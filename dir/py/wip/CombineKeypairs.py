import os

def query_all_wallets(address):

	wallet_file = [filename for filename in os.listdir("../wallets") if filename.endswith(".txt")]
	
	current_wallet = open(wallet_file, "r")
			
	search_keyword_in_file = current_wallet.readlines()

	for text_lines in search_keyword_in_file:
	
		keyword_is_Address = "Line 4"
		
		if text_lines.find(keyword_is_Address) == 0:
		
			# print("This is a wallet") # For testing
			
			Address_to_list = text_lines.split(" ")

			# print ("Combining address " + Address_to_list[9:67]) # For testing

			address = Address_to_list[9:67]			

	current_wallet.close()
