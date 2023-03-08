"""
Documentation of atomic transaction:
https://developer.algorand.org/docs/get-details/atomic_transfers/

Documentation of Algorand Python SDK:
1. https://developer.algorand.org/docs/sdks/python/
2. https://py-algorand-sdk.readthedocs.io/en/latest/

To do:
1. Iterate through every 16 batches in the lists "batchedTransactionInfo" and "batchedSignedTransaction"
2. Move spent addresses to spent directory
3. Test the program on testnet
4. Make program handle more than 16 transactions without error
5. Experiment on concurrent atomic transaction after sequential transaction is successful
"""

from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generatedAddress, generate_keypair
from algosdk import transaction
from AlgodUtils import algodClient
import os, shutil, json

numberOfKeypairs = [filename for filename in os.listdir("../wallet/") if filename.endswith(".txt")]\

def consolidate_balance():
	# Non sensitive data
	listTransacionInfo = []
	batchedTransactionInfo = []
	params = algodClient.suggested_params()	
	generate_keypair()
	toOwnAddress = generatedAddress

	for remainingUtxos in range(numberOfKeypairs):
		spendingCurrentUtxo = query_address()[remainingUtxos - 1]
		jsonTransactionInfo = transaction.PaymentTxn(spendingCurrentUtxo, params, toOwnAddress, balanceInMicroAlgos)
		listTransactionInfo.append(jsonTransactionInfo)

	for batchingListTransactionInfo in range(0, len(listTransactionInfo), 16):
		sixteenTransactions = listTransactionInfo[batchingList:batchingListTransactionInfo + 16]
		batchedTransactionInfo.append(sixteenTransactionInfo)
	groupId = transaction.calculate_group_id(listTransactionInfo)

	for individualTxId in range(len(batchedTransacionInfo)):
		individualTxId = GroupId

	# Sensitive data, private keys involved
	listPrivateKeys = []
	listSignedTransactions = []
	batchedSignedTransactions = []

	for numberOfPrivateKeys in range(len(numberOfKeypairs)):
		listPrivateKey.append(query_private_key()[numberOfPrivateKeys - 1])

	for transactionsToSign in range(len(listPrivateKeys)):
		signedIndividualTransaction = batchedTransactionInfo[transactionsToSign - 1].sign(listPrivateKeys[transactionsToSign - 1])
		listSignedTransactions.append(signedIndividualTransaction)

	for batchingSignedTransactions in range(0, len(listSignedTransactions), 16):
		sixteenSignedTransactions = listSignedTransaction [batchingSignedTransactions:batchingSignedTransactions + 16]
    		batchedSignedTransactions.append(sixteenSignedTransactions)

	for batchesOfSignedTransaction in range(len(batchedSignedTransaction)):
		transactionId = algodClient.send_transactions(batchedSignedTransaction[batchedSignedTransaction - 1])
		transactionConfirmed = wait_for_confirmation(algodClient, transactionId, 10)
		print("Transaction ID: {} ".format(transactionId), "confirmed in round {}.".format(transactionConfirmed.get("confirmed-round", 0)))

if __name__ == "__main__":
	consolidate_balance()