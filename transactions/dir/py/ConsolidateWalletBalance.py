"""
Documentation of atomic transaction:
https://developer.algorand.org/docs/get-details/atomic_transfers/

Documentation of Algorand Python SDK:
1. https://developer.algorand.org/docs/sdks/python/
2. https://py-algorand-sdk.readthedocs.io/en/latest/

To do:
1. Test the program on testnet
2. Make program handle more than 16 transactions without error
3. Experiment on concurrent atomic transaction after sequential transaction is successful
"""

from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generatedAddress, generate_keypair
from FilePaths import unspentUtxoPath, spentUtxoPath
from algosdk import transaction
from AlgodUtils import algodClient
import os, shutil

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def consolidate_balance():
	listUnsignedTx = []
	batchedUnsignedTx = []
	listSignedTx = []
	batchedSignedTx = []
	params = algodClient.suggested_params()
	generate_keypair()
	toOwnAddress = generatedAddress

	# For testing
	# print(listOfKeypairs)

	for remainingUtxos in range(len(listOfKeypairs)):
		currentUtxo = query_address()[remainingUtxos - 1]
		currentUtxoInfo = algodClient.account_info(currentUtxo)
		balanceInMicroAlgos = currentUtxoInfo.get('amount')

		if balanceInMicroAlgos != int(0):
			currentUnsignedTx = transaction.PaymentTxn(currentUtxo, params, toOwnAddress, balanceInMicroAlgos)
			listUnsignedTx.append(currentUnsignedTx)

			# Next 1 line has sensitive data, private keys involved
			signedTx = currentUnsignedTx.sign(query_private_key()[remainingUtxos - 1])
			# For testing
			# print(signedTx)
			listSignedTx.append(signedTx)
			listOfKeypairs[remainingUtxos - 1].close()
			shutil.move(listOfKeypairs[remainingUtxos - 1], spentUtxoPath)

	for batchingListTxInfo in range(0, len(listUnsignedTx), 16):
		batchingUnsignedTx = listUnsignedTx[batchingListTxInfo:batchingListTxInfo + 16]
		batchedUnsignedTx.append(batchingUnsignedTx)

	for batchingListTxInfo in range(0, len(listSignedTx), 16):
		batchingSignedTx = listSignedTx[batchingListTxInfo:batchingListTxInfo + 16]
		batchedSignedTx.append(batchingSignedTx)

	for txBatch in range(len(batchedSignedTx)):
		# For testing
		# print(batchedSignedTx[txBatch - 1])
		txId = algodClient.send_transactions(batchedSignedTx[txBatch - 1])
		confirmedTx = wait_for_confirmation(algodClient, txId, 10)
		print("txID: {}".format(txId), " confirmed in round: {}".format(confirmedTx.get("confirmed-round", 0)))

	for txBatches in range(len(batchedUnsignedTx)):
		groupId = transaction.calculate_group_id(batchedUnsignedTx[txBatches - 1])

	for countUnsignedTx in range(len(listUnsignedTx)):
		listUnsignedTx[countUnsignedTx - 1] = groupId

	for txBatch in range(len(batchedSignedTx)):
		txId = algodClient.send_transaction(batchedSignedTx[txBatch - 1])
		confirmedTx = wait_for_confirmation(algodClient, txId, 10)
		print("txID: {}".format(txId), " confirmed in round: {}".format(confirmedTx.get("confirmed-round", 0)))

if __name__ == "__main__":
	if len(listOfKeypairs) != int(0):
		consolidate_balance()
	else:
		print("\n\nYou Have Not Generated A Keypair Yet")
		print("\n\nPlease Create A New Keypair And Fund It")
