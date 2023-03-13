from encryption.Encrypt import encrypt_plaintext
from FilePaths import unspentUtxoPath
from algosdk import account, mnemonic

generatedPrivateKey, generatedAddress = account.generate_account()

def generate_keypair ():
	with open(unspentUtxoPath+generatedAddress+".txt", "x") as newDocumentPath
		newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
		encryptedPrivateKey = encrypt_plaintext("Seed: {}" .format(mnemonic.from_private_key(generatedPrivateKey)))
		newDocumentPath.write(encryptedPrivateKey)
	if __name__ == "__main__":
		print("\n\nAddress: {}" .format(generatedAddress))
		print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")

if __name__ == "__main__":
	generate_keypair()
