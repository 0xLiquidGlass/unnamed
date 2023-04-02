"""
Written by Liquid Glass

Documentation for standard transactions: https://developer.algorand.org/docs/sdks/python/

Note that this library can only handle 1 transaction at one go. Any transaction that
requires more than 1 individual transaction please check the AtomicTxUtils library

Useable functions when imported:

1. initiate_unsigned_normal_tx(currentUtxo, receivingAddress, sendAmount)

This function will prepare a standard transaction, returns the prepared transaction

2. sign_unsigned_normal_tx(thisUnsignedTx, correspondingPrivateKey)

This function will take the prepared transaction and will be passed to the thisUnsignedTx
parameter and then signs the prepared transaction with the corresponding private key

Returns the signed transaction

3. broadcast_signed_normal_tx(signedTx)

This function will broadcast (or send) your signed transaction that is passed into the signedTx parameter

If successful, prints the transaction ID and the block that the transaction was confirmed on
"""

from globals.AlgodUtils import algodClient
from algosdk import transaction

params = algodClient.suggested_params()

def initiate_unsigned_normal_tx(currentUtxo, receivingAddress, sendAmount):
        unsignedTx = transaction.PaymentTxn(currentUtxo, params, receivingAddress
                                            , sendAmount, receivingAddress)
        return unsignedTx

def sign_unsigned_normal_tx(thisUnsignedTx, correspondingPrivateKey):
        signedThisTx = thisUnsignedTx.sign(correspondingPrivateKey)
        return signedThisTx

def broadcast_signed_normal_tx(signedTx):
        txId = algodClient.send_transaction(signedTx)
        confirmedTx = transaction.wait_for_confirmation(algodClient, txId, 10)
        print("\nTransaction ID: {}" .format(txId))
        print("\nConfirmed in round {}" .format(confirmedTx.get("confirmed-round", 0)))
