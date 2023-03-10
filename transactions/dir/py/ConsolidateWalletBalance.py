"""
Documentation of atomic transaction:
https://developer.algorand.org/docs/get-details/atomic_transfers/

Documentation of Algorand Python SDK:
1. https://developer.algorand.org/docs/sdks/python/
2. https://py-algorand-sdk.readthedocs.io/en/latest/

To do:
1. Move spent addresses to spent directory
2. Test the program on testnet
3. Make program handle more than 16 transactions without error
4. Experiment on concurrent atomic transaction after sequential transaction is successful

Lines to take note of:
"""

from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generatedAddress, generate_keypair
from algosdk import transaction
from AlgodUtils import algodClient
import os, shutil

numberOfKeypairs = [filename for filename in os.listdir("../wallet/") if filename.endswith(".txt")]\

def consolidate_balance():
	listUnsignedTx = []
	batchedUnsignedTx = []
	listSignedTx = []
	batchedSignedTx = []
	params = algodClient.suggested_params()	
	generate_keypair()
	toOwnAddress = generatedAddress

	# For testing
	# print(numberOfKeypairs)

	for remainingUtxos in range(len(numberOfKeypairs)):
		currentUtxo = query_address()[remainingUtxos - 1]
		currentUtxoInfo = algodClient.account_info(currentUtxo)
		balanceInMicroAlgos = currentUtxoInfo.get('amount')
		currentUnsignedTx = transaction.PaymentTxn(currentUtxo, params, toOwnAddress, balanceInMicroAlgos)
		listUnsignedTx.append(currentUnsignedTx)

		# Next 1 line has sensitive data, private keys involved
		signedTx = currentUnsignedTx.sign(query_private_key()[remainingUtxos - 1])

		listSignedTx.append(signedTx)

	for batchingListTxInfo in range(0, len(listUnsignedTx), 16):
		batchingUnsignedTx = listUnsignedTx[batchingListTxInfo:batchingListTxInfo + 16]
		batchedUnsignedTx.append(batchingUnsignedTx)

	for batchingListTxInfo in range(0, len(listSignedTx), 16):
		batchingSignedTx = listSignedTx[batchingListTxInfo:batchingListTxInfo + 16]
		batchedSignedTx.append(batchingSignedTx)

	for txBatches in range(len(batchedUnsignedTx)):
		groupId = transaction.calculate_group_id(batchedUnsignedTx[txBatches - 1])

	for countUnsignedTx in range(len(listUnsignedTx)):
		listUnsignedTx[countUnsignedTx - 1] = groupId

	for txBatch in range(len(batchedSignedTx)):
		txId = algodClient.send_transaction(batchedSignedTx[txBatch - 1])
		confirmedTx = wait_for_confirmation(algodClient, txId, 10)
		print("txID: {}".format(txId), " confirmed in round: {}".format(confirmedTx.get("confirmed-round", 0)))

if __name__ == "__main__":
	consolidate_balance()