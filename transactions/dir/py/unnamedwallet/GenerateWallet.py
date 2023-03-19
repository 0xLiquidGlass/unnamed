from encryption.PasswordUtils import prompt_key, stretchedKey
from encryption.Encrypt import encrypt_plaintext
from globals.FilePaths import unspentUtxoPath
from algosdk import account, mnemonic

generatedPrivateKey, generatedAddress = account.generate_account()

def generate_keypair(stretchedKey):
	with open(unspentUtxoPath+generatedAddress+".txt", "x") as newDocumentPath
		newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
		plainSeedPhrase = ("Seed: {}" .format(mnemonic.from_private_key(generatedPrivateKey)))
		encryptedSeedPhrase = encrypt_plaintext(plainSeedPhrase, stretchedKey)
		newDocumentPath.write(encryptedSeedPhrase)
	if __name__ == "__main__":
		print("\n\nAddress: {}" .format(generatedAddress))
		print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")

if __name__ == "__main__":
	prompt_key()
	while True:
		try:
			numberOfKeypairs = int(input("\n\nNumber of addresses to generate: "))
			for generatingKeypairs in range(numberOfKeypairs):
				generate_keypair(stretchedKey)
			break
		except:
			print ("\n\nPlease try again")
		except OverflowError:
			print ("\n\nSeriously???")
