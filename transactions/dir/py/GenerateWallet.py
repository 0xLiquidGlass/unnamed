from algosdk import account, mnemonic

generatedPrivateKey, generatedAddress = account.generate_account()

def generate_keypair ():
	newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
	newDocumentPath.write("Seed: {}" .format(mnemonic.from_private_key(generatedPrivateKey)))

def keypair_generate_prompt():
        filename = input("Name of File: ")
        newDocumentPath = open(filename+".txt", "x")
        generate_keypair()
        newDocumentPath.close()
        print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")

if __name__ = "__main__":
        keypair_generate_prompt()
