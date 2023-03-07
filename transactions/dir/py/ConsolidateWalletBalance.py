"""
Documentation of atomic transaction:
https://developer.algorand.org/docs/get-details/atomic_transfers/

Documentation of Algorand Python SDK:
1. https://developer.algorand.org/docs/sdks/python/
2. https://py-algorand-sdk.readthedocs.io/en/latest/

To do:
1. Move spent addresses to spent directory
2. Test the program
"""

from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generatedAddress, generate_keypair, keypair_generate_prompt
from algosdk import transaction
from algodUtils import algod_init
from algosdk.future.transaction import *

# In case there is a need
import os

createTransactionsPool = []
signedTransactionsPool = []
splitSignedTransactionsPool = []
listPrivateKeys =[]
numberOfKeypairs = [filename for filename in os.listdir("../wallet") if filename.endswith(".txt")]\

def prepare_transactions_info():
    utxosLeft = len(numberOfKeypairs)
    for counter in utxosLeft:
        keypair_generate_prompt()
        # Non sensitive data (4 lines below)
        toHomeConst = generatedAddress
        utxoAddress = query_address()
        balance = algod_init.account_info(utxoAddress)
        valueMicroAlgos = balance
        transactionsInfo = transaction.PaymentTxn(utxoAddress, params, toHomeConst, valueMicroAlgos)
        transactionsPool.append(transactionsInfo)
        # Sensitive data, private keys and mnemonics involved (2 lines below)
        utxoPrivateKey = query_private_key()
        listPrivateKeys.append(utxoPrivateKey)

def atomic_transactions_prepare():
    # Non sensitive data (3 lines below)
    everyTransactionsGroupID = transaction.calculate_group_id([createTransactionsPool])
    for countTransactions in createTransactionsPool:
        countTransactions.group = everyTransactionsGroupID
    # Sensitive data, private keys involved (3 lines below)
    for countSignKeys in listPrivateKeys:
        signTransactionInfo = everyTransactionsGroupID.sign(countSignKeys)
        signedTransactionsPool.append(signTransactionsPool)

def atomic_transactions_execute():
    for splitCounter in range (0, len(signedTransactionsPool), 16):
        splitSignedTransactionsPool.append(signedTransactionsPool[splitCounter:splitCounter+16])
    for countSplitSignedTransactions in splitSignedTransactionsPool:
        iterateSplitSignedTransactions = splitSignedTransactionsPool[countSplitSignedTransaction]
    	signedTransactions = splitSignedTransactionsPool
    	TransactionID = algod_init.send_transactions(signedTransactions)
    	confirmedTransaction = wait_for_confirmation (algod_init, TransactionID, 15)
    	print("txID: {}".format(TransactionID), " confirmed in round: {}".format(confirmedTransaction.get("confirmed-round", 0)))   
    
if __name__ == "__main__":
