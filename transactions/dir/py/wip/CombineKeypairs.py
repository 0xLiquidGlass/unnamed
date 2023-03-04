from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
import os

keypairs_counted = 0

def query_every_wallet(address):
	wallet_file = [filename for filename in os.listdir(".") if filename.endswith(".txt")]\
	total_keypairs = len(wallet_file)
	current_wallet = open(wallet_file, "r")
	search_keyword_in_file = current_wallet.readlines()

	for text_lines in search_keyword_in_file:
		keyword_is_Address = "Line 1"
		if text_lines.find(keyword_is_Address) == 0:
			# For testing 
			# print("This is a wallet")
			Address_to_list = text_lines.split(" ")
			# For testing (line 25)
			# print ("Combining address " + Address_to_list[9:67])
			address = Address_to_list[9:67]
			keypairs_counted += 1
	current_wallet.close()

def query_private_key(private_key):
        wallet_file = [filename for filename in os.listdir(".") if filename.endswith(".txt")]\
	total_keypairs = len(wallet_file)
	current_wallet = open(wallet_file, "r")
	search_keyword_in_file = current_wallet.readlines()

	for text_lines in search_keyword_in_file:
		keyword_is_Seed = "Line 3"
		if text_lines.find(keyword_is_Seed) == 0:
			# For testing (line 19)
			# print("This is a wallet")
			Seed_to_list = text_lines.split(" ")
			# For testing (line 25)
			# print ("Showing Seed Phrase: " + Seed_to_list[1:26])
			seed_phrase = Seed_to_list[1:26]
			keypairs_counted += 1
	current_wallet.close()
