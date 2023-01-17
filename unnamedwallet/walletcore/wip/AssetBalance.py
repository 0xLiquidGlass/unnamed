# (temp hacky implementation of Total asset balance of the user, 
# this file would need refactoring later)
from algosdk.v2client import algod
import CombineKeypairs
from utils.algodinstance import algodinstance
# Load algod and kmd endpoints and respective tokens
import os
from dotenv import load_dotenv
load_dotenv()

# globals 
total_balance_in_microalgos = 0
algod_client = algodinstance().getclient()

# Query total balance of the user
def query_total_balance():
	global total_balance_in_microalgos
	global algod_client
	# get all addresses 
	all_wallets = CombineKeypairs.query_every_user_wallet()
	# call account_info() for every wallet and calculate total balance
	for i in range(len(all_wallets)):
		account_info = algod_client.account_info(all_wallets[i])
		total_balance_in_microalgos += account_info.get("amount")
		print(f'{i+1}: {all_wallets[i]} | Balance: {account_info.get("amount")}')

# Show total balance the user have
def show_total_balance():
	print ("Balance: {:.2f} Algos" . format(total_balance_in_microalgos*(10**-6)))

# query_total_balance()
# show_total_balance()
