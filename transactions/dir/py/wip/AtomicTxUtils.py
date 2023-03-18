from globals.AlgodUtils import algodClient
from algosdk import transaction
import os, shutil

params = algodClient.suggested_params()
listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

listUnsignedTx = []
listBatchedUnsignedTx = []
listSignedTx = []
listBatchedSignedTx = []

# Sensitive data, private keys involved
listDecryptedPrivateKey = []

def prepare_unsigned_tx(currentUtxo, params, receivingAddress, amount):
        unsignedTx = transaction.PaymentTxn(currentUtxo, params, receivingAddress, amount)
        listUnsignedTx.append(unsignedTx)

def prepare_sign_unsigned_tx(listDecryptedPrivateKey):
        # Sensitive data, private keys involved
        for currentUnsignedTx in len(listUnsignedTx):
                privateKey = listDecryptedPrivateKey[currentUnsignedTx]
                signedTx = listUnsignedTx[currentUnsignedTx].sign(privateKey)
                listSignedTx.append(signedTx)

def batch_unsigned_tx():
        for numberOfUnsignedTx in range(0, len(listUnsignedTx), 16):
                batchedUnsignedTx = listUnsignedTx[numberOfUnsignedTx:numberOfUnsignedTx + 16]
                listBatchedUnsignedTx.append(batchedUnsignedTx)

def batch_signed_tx():
        for numberOfSignedTx in range(0, len(listSignedTx), 16):
                batchedSignedTx = listSignedTx[numberOfSignedTx:numberOfSignedTx + 16]
                listBatchedSignedTx.append(batchedSignedTx)

def calculate_batched_groupid():
        for currentBatchedUnsignedTx in listBatchedUnsignedTx:
                groupId = transaction.calculate_group_id(currentBatchedUnsignedTx)
                calculate_individual_groupid(currentBatchedUnsignedTx)

def calculate_individual_groupid(currentBatchedUnsignedTx):
        for currentUnsignedTx in currentBatchedUnsignedTx:
                currentUnsignedTx.group = groupId

def send_transaction_group():
        for currentBatchedSignedTx in listBatchedSignedTx:
                txId = algodClient.send_transactions(currentBatchedSignedTx)
                confirmedTx = wait_for_confirmation(algodClient, txId, 10)
                print("\n\ntxId: {} ".format(txId), "confirmed in round {}" .format(confirmedTx.get("confirmed-round", 0)))
