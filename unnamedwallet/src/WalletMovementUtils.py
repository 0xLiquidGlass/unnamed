"""
Written by Liquid Glass

Useable functions when imported:

1. move_utxo_to_unsafe_dir(currentUtxoIndex)

This function is useful when you want to move a keypair, whose UTXO (or account)
has dust, and would like to be moved from the unspent/ directory to the unsafe/ 
directory as this UTXO can harm one's privacy

2. move_utxo_to_spent_dir(currentUtxoIndex)

This function is useful when you want to move keypairs that has already been signed
or spent from the unspent/ directory to the spent/ directory

Returns the filename of the keypair moved

3. unmove_spent_utxos(listMovedKeypairs, changeAddress)

This function is useful when you want to move moved keypairs back to unspent/ directory
from the spent/ directory (e.g. due to interruptions like ctl + c, etc)

If there is no change address, simply put None in the changeAddress parameter

Note: Requires a list of keypairs that has been moved to spent/ directory during runtime

4. revert_moved_utxo(listMovedKeypairs, listChangeAddress)

This function when called, will prepare the list of keypairs that has been moved to the
spent directory and the change address generated to revert it back to the state before
the session started to move keypairs when they are spent and a change address has not yet
been created (i.e. removed)

However, if the change address has a positive balance, the change address will not be
removed
"""

from globals.AlgodUtils import algodClient
from globals.FilePaths import unspentUtxoPath, spentUtxoPath, unsafeUtxoPath
import os, shutil

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def move_utxo_to_unsafe_dir(currentUtxoIndex):
        currentKeypair = listOfKeypairs[currentUtxoIndex]
        shutil.move((unspentUtxoPath + currentKeypair), unsafeUtxoPath)
        print("\nThe unsafe UTXO has been moved")

def move_utxo_to_spent_dir(currentUtxoIndex):
        currentKeypair = listOfKeypairs[currentUtxoIndex]
        shutil.move((unspentUtxoPath + currentKeypair), spentUtxoPath)
        # For testing
        # print("\n{} has been moved" .format(currentKeypair))
        return currentKeypair

def unmove_spent_utxos(listMovedKeypairs, changeAddress):
        for currentKeypair in listMovedKeypairs:
                shutil.move((spentUtxoPath + currentKeypair), unspentUtxoPath)
        remove_change_wallet(changeAddress)
        # For testing
        # print("\n{} has been reverted back to unspent" .format(currentKeypair))

def remove_change_wallet(changeAddress):
        if changeAddress != None:
                os.remove(unspentUtxoPath + changeAddress + ".txt")
                # print("\nThe newly generated address {} has been removed from spent/ directory successfully" .format(changeAddress))

def revert_moved_utxo(listMovedKeypairs, listChangeAddress):
        changeAddress = listChangeAddress[0]
        changeAccountInfo = algodClient.account_info(changeAddress)
        changeAccountBalance = changeAccountInfo.get("amount")
        if changeAccountBalance > float(0):
                unmove_spent_utxos(listMovedKeypairs, None)
        else:
                unmove_spent_utxos(listMovedKeypairs, changeAddress)

        print("\n\nThe process has been interrupted")
        print("\nMoving all spent UTXOs back to unspent")
        exit(1)
