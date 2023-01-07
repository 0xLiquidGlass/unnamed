import os
# This function is responsible for total balance calculation of a user
# Get all wallets of the user from "wallets" dir
# Collect total balance available in terms of microalgo 
# change: function name for query_every_wallet, to query_every_user_wallet

# Note: these base methods will change once we implement ECIES 
# to encrypt wallets as they are generated for better security measures
# Reference: https://cryptobook.nakov.com/asymmetric-key-ciphers/ecies-example

# Create a list of wallets, so that we can query each one easily in assetbalance 
def query_every_user_wallet() -> list: # we return list of addresses
	# Get all present wallets
	wallet_files = [filename for filename in os.listdir("../wallets/") if filename.endswith(".txt")]
	# Don't need "total_keypairs" as of now, we can later use len(wallet_file) to reference to total wallets present in the system
	# as wallet(s) should be deleted once one or more wallets are consumed as input utxo, 
	# and it should result into one or more output wallets (output utxo in a sense)
	## total_keypairs = len(wallet_file)
	print(f'Total wallets: {len(wallet_files)}')
	wallet_addresses = []
	for wallet in wallet_files:
		# open that wallet file and read address line
		with open('../wallets/'+wallet) as wal:
			wallet_addresses.append(wal.readline().split(':')[1].strip())	# pub address
	return wallet_addresses # can be empty list if no wallets created yet

print(query_every_user_wallet())
