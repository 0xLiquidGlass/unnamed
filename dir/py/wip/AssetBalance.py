#requires CombineKeypairs.py
from algosdk import account, mnemonic
from algosdk.v2client import algod
import CombineKeypairs
# Load algod and kmd endpoints and respective tokens
import os
from dotenv import load_dotenv
load_dotenv()

total_balance_in_microalgos = 0

algod_address = os.getenv("ALGOD_ADDRESS")
algod_token = os.getenv("ALGOD_TOKEN")

algod_client = algod.AlgodClient(algod_token, algod_address)

def query_balance_per_address(address):
	
	account_info = algod_client.account_info(CombineKeypairs.query_every_wallet(address))

	total_balance_in_microalgos += account_info.get("amount")

def show_total_balance():
	print ("Your Balance: {:.2f} Algos" . format(total_balance_in_microalgos*(10**-6)))
	while (keypairs_counted <= total_keypairs):
		query_balance_per_addresss()

show_total_balance()
