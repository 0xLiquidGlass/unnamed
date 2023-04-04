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

3. unmove_spent_utxos(listMovedKeypairs)

this function is useful when you want to move moved keypairs back to unspent/ directory
from the spent/ directory (e.g. due to interruptions like ctl + c, etc)

Note: Requires a list of keypairs that has been moved to spent/ directory during runtime
"""

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

def unmove_spent_utxos(listMovedKeypairs):
        for currentKeypair in listMovedKeypairs:
                shutil.move((spentUtxoPath + currentKeypair), unspentUtxoPath)
        # For testing
        # print("\n{} has been reverted back to unspent" .format(currentKeypair))
