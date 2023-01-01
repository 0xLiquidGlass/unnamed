from algosdk import account, mnemonic

from algosdk.v2client import algod

import CombineKeypairs

total_balance_in_microalgos = 0

def what_is_my_balance():

	algod_address = "node.algoexplorerapi.io/"

	algod token = ""

	algod_client = algod.AlgodClient(algod_token, algod_address)

	# Obtain balance through one address at a time

	account_info = algod_client.account_info(CombineKeypairs.query_all_wallets(address))

	total_balance_in_microalgos += acccount_info.get("amount")
	
	print ("Your Balance: {:.2f} Algos" . format(total_balance_in_microalgos*(10**-6)))

while True:	

	what_is_my_balance()