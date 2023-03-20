from globals.AlgodUtils import algodClient
from globals.FilePaths import unspentUtxoPath, spentUtxoPath
from CombineKeypairs import query_address, query_private_key
from algosdk import transaction
import os, shutil

params = algodClient.suggested_params()
listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

listUnsignedTx = []
listBatchedUnsignedTx = []
listSignedTx = []
listBatchedSignedTx = []

def unsigned_tx_type_prepare(txType, receivingAddress, sendingMicroAlgos):
        if txType == "internal":
                prepare_unsigned_tx(receivingAddress, "all")
        elif txType == "external":
                prepare_unsigned_tx(receivingAddress, sendingMicroAlgos)

def prepare_unsigned_tx(receivingAddress, sendingMicroAlgos):
        for keypairIndex in len(listOfKeypairs):
                currentUtxo = query_address()[keypairIndex]
                utxoInfo = algodClient.account_info(currentUtxo)
                utxoBalance = utxoInfo.get("amount")
                try:
                        check_utxo_positive_balance(utxoBalance)
                        regular_change_unsigned_tx(sendingMicroAlgos, currentUtxo, receivingAddress, utxoBalance)
                except UtxoZeroBalance:
                        pass
                except UnsafeUtxoDust:
                        shutil.move(listOfKeypairs[keypairIndex], unsafeUtxoPath)
                        print("{} ".format(currentUtxo), "moved to the unsafe/ directory")
                except FinalTxWithChange:
                        break

def regular_change_unsigned_tx(sendingMicroAlgos, currentUtxo, receivingAddress, utxoBalance):
        if sendingMicroAlgos == "all":
                prepare_regular_tx(currentUtxo, receivingAddress, utxoBalance)
        else:
                prepare_tx_with_change(sendingMicroAlgos, currentUtxo, receivingAddress, utxoBalance)
                sendingMicroAlgos = sendingMicroAlgos - utxoBalance

def prepare_tx_with_change(sendingMicroAlgos, currentUtxo, utxoBalance, receivingAddress, utxoBalance):
        if sendingMicroAlgos > utxoBalance:
                prepare_regular_tx(currentUtxo, utxoBalance, receivingAddress, utxoBalance)
        else:
                prepare_change_tx(sendingMicroAlgos, currentUtxo, receivingAddress, utxoBalance)

def prepare_regular_tx(currentUtxo, receivingAddress, utxoBalance):
        unsignedTx = transaction.PaymentTxn(currentUtxo, params, receivingAddress, utxoBalance)
        listUnsignedTx.append(unsignedTx)

def prepare_change_tx(sendingMicroAlgos, currentUtxo, receivingAddress, utxoBalance):
        notChange = sendingMicroAlgos
        unsignedTx = transaction.PaymentTxn(currentUtxo, params, receivingAddress, notChange)
        listUnsignedTx.append(unsignedTx)
        isChange = utxoBalance - sendingMicroAlgos
        unsignedTx = transaction.PaymentTxn(currentUtxo, params, receivingAddress, isChange)
        listUnsignedTx.append(unsignedTx)
        raise FinalTxWithChange

def check_utxo_positive_balance(utxoBalance):
        if utxoBalance > int(0):
                pass
        else:
                raise UtxoZeroBalance

def check_utxo_no_dust(utxoBalance):
        integerDustLimit = int(transaction.SuggestedParams(fee)*3)
        if utxoBalance > integerDustLimit:
                pass
        else:
                raise UnsafeUtxoDust ("\n\nThis UTXO contains dust. Recommended to not use this UTXO")

def prepare_sign_unsigned_tx(txType, stretchedKey):
        # Sensitive data, private keys involved
        decryptPrivateKey = query_private_key(stretchedKey)
        for indexCurrentUnsignedTx in len(listUnsignedTx):
                if txType == "internal":
                        prepare_regular_signing(indexCurrentUnsignedTx)
                elif txType == "external":
                        regular_change_signing_switch(indexCurrentUnsignedTx)

def regular_change_signing_switch(indexCurrentUnsignedTx):
        if indexCurrentUnsignedTx > int(2):
                prepare_regular_signing(indexCurrentUnsignedTx)
        elif indexCurrentUnsignedTx <= int(2):
                prepare_signing_with_change(indexCurrentUnsignedTx)

def prepare_regular_signing(indexCurrentUnsignedTx):
        # Sensitive date, private keys involved
        decryptedPrivateKey = query_private_key()[indexCurrentUnsignedTx]
        signedTx = listUnsignedTx[indexCurrentUnsignedTx].sign(decryptedPrivateKey)
        listSignedTx.append(signedTx)

def prepare_signing_with_change(indexCurrentUnsignedTx):
        # Sensitive data, private keys involved
        prepare_regular_signing(indexCurrentUnsignedTx)
        decryptedPrivateKey = query_private_key()[indexCurrentUnsignedTx]
        signedTx = listUnsignedTx[indexCurrentUnsignedTx + 1].sign(decryptedPrivateKey)
        listSignedTx.append(signedTx)

def batch_unsigned_tx():
        for numberOfUnsignedTx in range(0, len(listUnsignedTx), 16):
                batchedUnsignedTx = listUnsignedTx[numberOfUnsignedTx:numberOfUnsignedTx + 16]
                listBatchedUnsignedTx.append(batchedUnsignedTx)

def batch_signed_tx():
        for numberOfSignedTx in range(0, len(listSignedTx), 16):
                batchedSignedTx = listSignedTx[numberOfSignedTx:numberOfSignedTx + 16]
                listBatchedSignedTx.append(batchedSignedTx)

def calculate_groupid():
        for currentBatchedUnsignedTx in listBatchedUnsignedTx:
                groupId = transaction.calculate_group_id(currentBatchedUnsignedTx)
                calculate_individual_groupid(currentBatchedUnsignedTx)

def calculate_individual_groupid(currentBatchedUnsignedTx):
        for currentUnsignedTx in currentBatchedUnsignedTx:
                currentUnsignedTx.group = groupId

def send_transaction_group():
        try:
                for currentBatchedSignedTx in listBatchedSignedTx:
                        txId = algodClient.send_transactions(currentBatchedSignedTx)
                        confirmedTx = wait_for_confirmation(algodClient, txId, 10)
                        print ("\n\ntxId: {} ".format(txId), "confirmed in round {}" .format(confirmedTx.get("confirmed-round", 0)))
                print ("\n\nAll transactions have been completed")
        except algosdk.error.AlgodHTTPError:
                print ("\n\nSandbox has not started yet. Quit this app and restart")
                exit(1)
