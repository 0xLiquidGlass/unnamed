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
from globals.FilePaths import unspentUtxoPath
from globals.ValueConstants import txFeeConst
from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generate_keypair
from globals.AlgodUtils import algodClient
import WalletMovementUtils as WalletMovement
import NormalTxUtils as NormalTx
import AtomicTxUtils as AtomicTx
import AtomicTxErrors as BalanceCheck
import os

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

listChangeAddress = []
listMovedKeypairs = []

# Sensitive data, private keys involved
listRelevantPrivateKeys = []

countFrom = int(0)

def consolidate_wallet_balance():
        obtainedKey = get_key()

        listOfUtxos = query_address()

        # Sensitive data, private keys involved
        listOfPrivateKeys = query_private_key(obtainedKey)

        generatedSalt = generate_kdf_salt()
        newStretchedKey = stretch_key(obtainedKey, generatedSalt)
        receivingAddress = generate_keypair(generatedSalt, newStretchedKey)
        listChangeAddress.append(receivingAddress)

        countUpTo = len(listOfUtxos)
        countIncrement = int(1)

        for currentUtxoIndex in range(countFrom, countUpTo, countIncrement):
                currentUtxo = listOfUtxos[currentUtxoIndex]
                # Sensitive data, private keys involved
                currentPrivateKey = listOfPrivateKeys[currentUtxoIndex]
                if currentPrivateKey == None:
                        print("\nThe private key for {} cannot be decrypted" .format(currentUtxo))
                        print("\nMoving on to the next one")
                        continue
                accountInfo = algodClient.account_info(currentUtxo)
                txFee = txFeeConst
                utxoBalance = (int(accountInfo.get("amount")) - txFee)

                localErrorCodeReturned = BalanceCheck.check_valid_utxo(currentUtxo)

                if localErrorCodeReturned == int(0):
                        AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, utxoBalance
                                                      , receivingAddress)
                        preparedNormalTx = NormalTx.initiate_unsigned_normal_tx(currentUtxo
                                                                                , receivingAddress
                                                                                , utxoBalance
                                                                                , receivingAddress)

                        # Sensitive data, private keys involved
                        listRelevantPrivateKeys.append(currentPrivateKey)

                        movedUtxo = WalletMovement.move_utxo_to_spent_dir(currentUtxoIndex)
                        listMovedKeypairs.append(movedUtxo)

                elif localErrorCodeReturned == int(1):
                        continue

                elif localErrorCodeReturned == int(2):
                        WalletMovement.move_utxo_to_unsafe_dir(currentUtxoIndex)

        if len(listMovedKeypairs) == int(1):
                # For testing
                # print("\nUsed NormalTxUtils library")

                AtomicTx.listUnsignedTx.clear()

                correspondingPrivateKey = listRelevantPrivateKeys[0]

                signedNormalTx = NormalTx.sign_unsigned_normal_tx(preparedNormalTx
                                                                  , correspondingPrivateKey)

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


if __name__ == "__main__":
        try:
                if len(listOfKeypairs) == int(0):
                        print("\nYou do not have any UTXOs yet")
                        print("\nMake a new UTXO and fund it before consolidating your UTXOs")
                        exit(0)

                else:
                        consolidate_wallet_balance()

        except:
                WalletMovement.revert_moved_utxo(listMovedKeypairs, listChangeAddress)
