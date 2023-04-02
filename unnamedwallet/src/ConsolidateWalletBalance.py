"""
Written by Liquid Glass

Useable functions when imported:

1. consolidate_wallet_balance()

Where this function will check if the UTXO (or account) is good for spending, 
prepare the transactions individually and finally depending on how many individual
transactions are there, will choose either the normal transaction (which handles
1 transaction only) or an atomic transaction (which handles more than 1 transaction
but the transaction will be broadcasted in batches of 16 individual transactions)
"""

from PasswordUtils import get_key, generate_kdf_salt, stretch_key
from globals.FilePaths import unspentUtxoPath, spentUtxoPath, unsafeUtxoPath
from globals.ValueConstants import txFeeConst
from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generate_keypair
from globals.AlgodUtils import algodClient
import NormalTxUtils as NormalTx
import AtomicTxUtils as AtomicTx
import AtomicTxErrors as BalanceCheck
import os, shutil

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

listMovedKeypairs = []

# Sensitive data, private keys involved
listRelevantPrivateKeys = []

def consolidate_wallet_balance():
        obtainedKey = get_key()

        listOfUtxos = query_address()

        # Sensitive data, private keys involved
        listOfPrivateKeys = query_private_key(obtainedKey)

        generatedSalt = generate_kdf_salt()
        newStretchedKey = stretch_key(obtainedKey, generatedSalt)
        receivingAddress = generate_keypair(generatedSalt, newStretchedKey)

        for currentUtxoIndex in range(len(listOfUtxos)):
                currentUtxo = listOfUtxos[currentUtxoIndex]
                accountInfo = algodClient.account_info(currentUtxo)
                txFee = txFeeConst
                utxoBalance = (int(accountInfo.get("amount")) - txFee)

                localErrorCodeReturned = BalanceCheck.check_valid_utxo(currentUtxo)

                if localErrorCodeReturned == int(0):
                        AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, utxoBalance)
                        preparedNormalTx = NormalTx.initiate_unsigned_normal_tx(currentUtxo
                                                                                , receivingAddress
                                                                                , utxoBalance)

                        # Sensitive data, private keys involved
                        currentPrivateKey = listOfPrivateKeys[currentUtxoIndex]
                        listRelevantPrivateKeys.append(currentPrivateKey)

                        movedUtxo = move_utxo_to_spent_dir(currentUtxoIndex)
                        listMovedKeypairs.append(movedUtxo)

                elif localErrorCodeReturned == int(1):
                        continue

                elif localErrorCodeReturned == int(2):
                        currentKeypair = listOfKeypairs[currentUtxoIndex]
                        shutil.move((unspentUtxoPath + currentKeypair), unsafeUtxoPath)
                        print("\nThe unsafe UTXO has been moved")

        if len(listMovedKeypairs) == int(1):
                # For testing
                # print("\nUsed NormalTxUtils library")

                AtomicTx.listUnsignedTx.clear()

                correspondingPrivateKey = listRelevantPrivateKeys[0]

                signedNormalTx = NormalTx.sign_unsigned_normal_tx(preparedNormalTx, correspondingPrivateKey)

                NormalTx.broadcast_signed_normal_tx(signedNormalTx)

        elif len(listMovedKeypairs) > int(1):
                # For testing
                # print("\nUsed AtomicTxUtils library")

                del preparedNormalTx

                AtomicTx.batch_every_unsigned_tx()

                AtomicTx.calculate_group_id()

                AtomicTx.sign_these_unsigned_txs(listRelevantPrivateKeys)

                AtomicTx.batch_every_signed_tx()

                AtomicTx.broadcast_atomic_txs()

def move_utxo_to_spent_dir(currentUtxoIndex):
        currentKeypair = listOfKeypairs[currentUtxoIndex]
        shutil.move((unspentUtxoPath + currentKeypair), spentUtxoPath)
        # For testing
        # print("\n{} has been moved" .format(currentKeypair))

def unmove_spent_utxos():
        for currentKeypair in listMovedKeypairs:
                shutil.move((spentUtxoPath + currentKeypair), unspentUtxoPath)
        # For testing
        # print("\n{} has been reverted back to unspent" .format(currentKeypair))

def initiate_revert_moved_utxo():
        unmove_spent_utxos()
        print("\n\nThe process has been interrupted")
        print("\nMoving all spent UTXOs back to unspent")
        exit(0)

if __name__ == "__main__":
        try:
                if len(listOfKeypairs) == int(0):
                        print("\nYou do not have any UTXOs yet")
                        print("\nMake a new UTXO and fund it before consolidating your UTXOs")
                        exit(0)

                else:
                        consolidate_wallet_balance()

        except:
                initiate_revert_moved_utxo()
