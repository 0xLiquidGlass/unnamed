from algosdk import account, mnemonic

# Perform new account generation
# @Todo: storing plaintext pub/seed is bad security practice. 
# We should find a way to encrypt these with user given password 
def generate_keypair ():
	wallet_file_name = input("Name of File: ")
	# Create that file, this can potentially replace existing wallets too
	# Todo: fix this way to wallet gathering 
	with open("../../wallets/"+wallet_file_name+".txt", "x") as wallet_file:
		private_key, address = account.generate_account()
		wallet_file.write("Address: {}\n\n" .format(address))
		wallet_file.write("Seed: {}" .format(mnemonic.from_private_key(private_key)))
		print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")

generate_keypair()