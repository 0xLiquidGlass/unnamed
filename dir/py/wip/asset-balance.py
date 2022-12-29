from algosdk import account, mnemonic

from algosdk.v2client import algod

def what_is_my_balance(private_key, address):

	algod_address = ""

	algod token = ""

	algod_client = algod.AlgodClient(algod_token, algod_address)

	account_info = algod_client.account_info(address)

	print ("Balance: {} Algos" .format(account_info.get("amount")) + "\n")

	
