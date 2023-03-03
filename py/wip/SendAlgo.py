# Credits to ChatGPT for helping in the development

from algosdk import account, encoding, transaction, algod
from algosdk.future import transaction as futuretxn
from algosdk.v2client import algod
import os

keypairs_counted = 0
total_balance = 0
transactions = []

def query_every_wallet_address():
	wallet_file = [filename for filename in os.listdir(".") if filename.endswith(".txt")]\
	total_keypairs = len(wallet_file)
	current_wallet = open(wallet_file, "r")
	search_keyword_in_file = current_wallet.readlines()
	for text_lines in search_keyword_in_file:
		keyword_is_Address = "Line 4"
		if text_lines.find(keyword_is_Address) == 0:
			# For testing (line 19)
			# print("This is a wallet")
			Address_to_list = text_lines.split(" ")
			# For testing (line 25)
			# print ("Combining address " + Address_to_list[9:67])
			address = Address_to_list[9:67]
                        asset_balance(address)
			keypairs_counted += 1		
	current_wallet.close()

def query_every_priv_key():
    	wallet_file = [filename for filename in os.listdir(".") if filename.endswith(".txt")]\
	total_keypairs = len(wallet_file)
	current_wallet = open(wallet_file, "r")
	search_keyword_in_file = current_wallet.readlines()
	for text_lines in search_keyword_in_file:
		keyword_is_Address = "Line 6"
		if text_lines.find(keyword_is_seed) == 0:
			# For testing (line 19)
			# print("This is a wallet")
			seed_to_list = text_lines.split(" ")
			# For testing (line 25)
			# print ("Combining address " + Address_to_list[9:67])
			private_key = Address_to_list[9:67]
                        asset_balance(address)
			keypairs_counted += 1		
	current_wallet.close()
    

def load_agod():
       algod_address = ""
       algod_token = ""
       algod_client = algod.AlgodClient(algod_token, algod_address)

def asset_balance(address):
     per_address_balance = algod_client.account_info(address)
     print("Account balance: {} Algos".format(account_info.get('amount'*(10^-6))) + "\n")

def utxo_query_info():
    

def atomic_utxo_send(private_key, sendto_address, amount_algos):
    for keypairs_left in keypairs_counted:
        sender = ""
        receiver = sendto_address #self declared variable
        params = algod_client.suggested_params()
        amount = amount_algos
        unsigned_txn = transaction.PaymentTxn(sender, params, receiver, amount)
        unsigned_txn.group = group_id
        signing_key = private_key
        signed_txn = unsigned_txn.sign(signing_key)
        transactions.append(signed_txn)

try:
    transactions_id = algod_client.send_transactions(txns)
    print("Transaction ID:", transactions_id)
except Exception as error_message:
    print("Error:", error_message)
