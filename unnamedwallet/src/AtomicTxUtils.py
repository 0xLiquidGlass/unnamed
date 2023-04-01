from globals.AlgodUtils import algodClient
from algosdk import transaction

params = algodClient.suggested_params()
# listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

listUnsignedTx = []
listBatchedUnsignedTx = []
listSignedTx = []
listBatchedSignedTx = []

def initiate_unsigned_tx(sendAddress, currentUtxo, sendAmount):
        preparedTx = transaction.PaymentTxn(sendAddress, params, currentUtxo, sendAmount)
        listUnsignedTx.append(preparedTx)

def batch_every_unsigned_tx():
        for currentUnsignedTx in range(len(listUnsignedTx)):
                batchedUnsignedTx = listUnsignedTx[currentUnsignedTx : currentUnsignedTx + 16]
                listBatchedUnsignedTx.append(batchedUnsignedTx)

def calculate_group_id():
        for currentBatchUnsignedTx in listBatchedUnsignedTx:
                transaction.assign_group_id(currentBatchUnsignedTx)

def sign_these_unsigned_txs(listOfPrivateKeys):
        for currentUnsignedTxIndex in range(len(listUnsignedTx)):
                currentUnsignedTx = listUnsignedTx[currentUnsignedTxIndex]
                correspondingPrivateKey = listOfPrivateKeys[currentUnsignedTxIndex]
                signedTx = currentUnsignedTx.sign(correspondingPrivateKey)
                listSignedTx.append(signedTx)

def batch_every_signed_tx():
        for currentSignedTx in range(len(listSignedTx)):
                batchedSignedTx = listSignedTx[currentSignedTx : currentSignedTx + 16]
                listBatchedSignedTx.append(batchedSignedTx)

def broadcast_atomic_txs():
        for currentBatchedSignedTx in listBatchedSignedTx:
                txId = algodClient.send_transactions(currentBatchedSignedTx)
                confirmedTx =  wait_for_confirmation(algodClient, txId, 10)
                print("\nTransaction ID: {}" .format(txId))
                print("Confirmed in round {}" .format(confirmedTx.get("confirmed-round", 0)))
