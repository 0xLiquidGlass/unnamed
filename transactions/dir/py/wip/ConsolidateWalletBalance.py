"""
Documentation of atomic transaction:
https://developer.algorand.org/docs/get-details/atomic_transfers/

To do: 

1. Implement a for loop that limits an atomic transactions pool to up to 16
individual transactions 
"""

from CombineKeypairs import query_address, query_private_key
from ..GenerateWallet import generatedAddress, generate_keypair, keypair_generate_prompt
from algosdk import encoding
from algosdk.v2client import algod
from algosdk.future.transaction import *

# In case there is a need
import os

createTransactionsPool = []
signedTransactionsPool = []
listPrivateKeys =[]
numberOfKeypairs = [filename for filename in os.listdir(".") if filename.endswith(".txt")]\

def prepare_transactions_info():
    utxosLeft = len(numberOfKeypairs)
    valueMicroAlgos = int(input ("Algos to send: ")) * 10**6
    for counter in utxosLeft:
        keypair_generate_prompt()
        # Non sensitive data
        toHomeConst = generatedAddress
        utxoAddress = query_address()
        transactionsInfo = transaction.PaymentTxn(utxoAddress, params, toHomeConst, valueMicroAlgos)
        transactionsPool.append(transactionsInfo)
        # Sensitive data, private keys and mnemonics involved
        utxoPrivateKey = query_private_key
        listPrivateKeys.append(utxoPrivateKey)

def atomic_transactions_prepare():
    # Non sensitive data
    everyTransactionsGroupID = transaction.calculate_group_id([createTransactionsPool])
    for countTransactions in createTransactionsPool:
        countTransactions.group = everyTransactionsGroupID
    # Sensitive data, private keys involved
    for countSignKeys in listPrivateKeys:
        signTransactionInfo = everyTransactionsGroupID.sign(countSignKeys)
        signedTransactionsPool.append(signTransactionsPool)

def atomic_transactions_execute():
    signedTransactions = signedTransactionsPool
    TransactionID = algodClient.send_transactions(signedTransactions)
    confirmedTransaction = confirmationStatus (algodClient, TransactionID, 15)
    print("txID: {}".format(TransactionID), " confirmed in round: {}".format(confirmedTransaction.get("confirmed-round", 0)))   

if __name__ == "__main__":
