from algosdk import account, mnemonic

from algosdk.v2client import algod

total_balance_in_microalgos = 0

def what_is_my_balance(address):

	algod_address = ""

	algod token = ""

	algod_client = algod.AlgodClient(algod_token, algod_address)

	account_info = algod_client.account_info(address)
	
	total_balance_in_microalgos += acccount_info.get("amount")
	
	print ("Your Balance: {:.2f} Algos" . format(total_balance_in_microalgos*(10**6)) + "\n")
