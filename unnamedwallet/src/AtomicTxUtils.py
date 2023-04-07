"""
Written by Liquid Glass

Documentation for atomic transactions: https://developer.algorand.org/docs/get-details/atomic_transfers/

Useable functions when imported:

Note that atomic transfers will require a minimum of TWO transactions for the transaction to go through

Each atomic transaction can handle a maximum of 16 individual transactions as of 2023 Apr 3

Otherwise, use NormalTxUtils library for just a single transaction

1. initiate_unsigned_tx(currentUtxo, receivingAddress, sendAmount)

This function will prepare the transaction parameters for ONE transaction and holds the prepared transaction

2. batch_every_unsigned_tx()

Where this function will batch all of the prepared transaction in batches of 16

3. calculate_group_id()

This function will calculate the hash for every atomic transaction batch

4. sign_these_unsigned_txs(relevantPrivateKeys)

This function will sign all of the prepared transactions (which is previously unsigned) with the correct
private key passed to the relevantPrivateKeys paramater

5. batch_every_signed_tx()

This function will group all of the individual signed transactions in batches of 16

6. broadcast_every_signed_txs()

This function will broadcast (or send) every batch of atomic transaction (that has 16 individual regular
transactions in it) and if successful, the transaction ID and the block which the transaction was confirmed
on will be printed as output
"""

from globals.AlgodUtils import algodClient
from algosdk import transaction

params = algodClient.suggested_params()

listUnsignedTx = []
listBatchedUnsignedTx = []
listSignedTx = []
listBatchedSignedTx = []

countFrom = int(0)

def initiate_unsigned_tx(currentUtxo, receivingAddress, sendAmount, closeToAddress):
        preparedTx = transaction.PaymentTxn(currentUtxo, params, receivingAddress, sendAmount
                                            , closeToAddress)
        # For testing
        # print(preparedTx)
        listUnsignedTx.append(preparedTx)

def batch_every_unsigned_tx():
        countUpTo = len(listUnsignedTx)
        countIncrement = int(16)
        for currentUnsignedTx in range(countFrom, countUpTo, countIncrement):
                batchedUnsignedTx = listUnsignedTx[currentUnsignedTx : currentUnsignedTx + 16]
                # For testing
                # print(batchedUnsignedTx)
                listBatchedUnsignedTx.append(batchedUnsignedTx)

def calculate_group_id():
        for currentBatchUnsignedTx in listBatchedUnsignedTx:
                transaction.assign_group_id(currentBatchUnsignedTx)

def sign_these_unsigned_txs(relevantPrivateKeys):
        countUpTo = len(listUnsignedTx)
        countIncrement = int(1)
        for currentUnsignedTxIndex in range(countFrom, countUpTo, countIncrement):
                currentUnsignedTx = listUnsignedTx[currentUnsignedTxIndex]
                correspondingPrivateKey = relevantPrivateKeys[currentUnsignedTxIndex]
                signedTx = currentUnsignedTx.sign(correspondingPrivateKey)
                listSignedTx.append(signedTx)

def batch_every_signed_tx():
        countUpTo = len(listSignedTx)
        countIncrement = int(16)
        for currentSignedTx in range(countFrom, countUpTo, countIncrement):
                batchedSignedTx = listSignedTx[currentSignedTx : currentSignedTx + 16]
                listBatchedSignedTx.append(batchedSignedTx)

def broadcast_atomic_txs():
        numberOfTransactions = len(listBatchedSignedTx)
        countUpTo = len(listBatchedSignedTx)
        countIncrement = int(1)
        print("\nYou have {} transactions in queue" .format(numberOfTransactions))
        print("\nDo not quit while the transaction is still in progress")
        for currentBatchedSignedTxIndex in range(countFrom, countUpTo, countIncrement):
                numberOfBatchesLeft = numberOfTransactions - (currentBatchedSignedTxIndex + int(1))
                print("\nNumber of batches left: {}" .format(numberOfBatchesLeft))
                currentTxBatch = listBatchedSignedTx[currentBatchedSignedTxIndex]
                txId = algodClient.send_transactions(currentTxBatch)
                confirmedTx =  transaction.wait_for_confirmation(algodClient, txId, 10)
                print("\nTransaction ID: {}" .format(txId))
                print("\nConfirmed in round {}" .format(confirmedTx.get("confirmed-round", 0)))
