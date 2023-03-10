from algosdk import account, mnemonic

generatedPrivateKey, generatedAddress = account.generate_account()

def generate_keypair ():
	newDocumentPath = open("../wallet/transaction/unspent/"+generatedAddress+".txt", "x")
	newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
	newDocumentPath.write("Seed: {}" .format(mnemonic.from_private_key(generatedPrivateKey)))	
	newDocumentPath.close()
	if __name__ == "__main__":
		print("\n\nAddress: {}" .format(generatedAddress))
		print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")

if __name__ == "__main__":
	generate_keypair()
