# Credits to ChatGPT for helping in the development

from algosdk import account, encoding, algod
from algosdk.v2client import algod
import os

keypairs_counted = 0
total_balance = 0

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

def load_agod():
        algod_address = ""
        algod_token = ""
        algod_client = algod.AlgodClient(algod_token, algod_address)
        
def asset_balance(address):
        per_address_balance = algod_client.account_info(address)
        print("Account balance: {} Algos".format(account_info.get('amount'*(10^-6))) + "\n")
        
