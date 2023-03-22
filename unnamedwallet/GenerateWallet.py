from PasswordUtils import get_key
from Encrypt import encrypt_plaintext
from globals.FilePaths import unspentUtxoPath
from globals.Encoding import encoding
from algosdk import account, mnemonic

generatedPrivateKey, generatedAddress = account.generate_account()

def generate_keypair(stretchedKey):
	with open(unspentUtxoPath+generatedAddress+".txt", "x") as newDocumentPath:
		newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
		plainSeedPhrase = ("Seed: {}" .format(mnemonic.from_private_key(generatedPrivateKey)))
		byteSeedPhrase = plainSeedPhrase.encode(encoding)
		encryptedSeedPhrase = encrypt_plaintext(byteSeedPhrase, stretchedKey)
		newDocumentPath.write(encryptedSeedPhrase)
	if __name__ == "__main__":
		print("\n\nAddress: {}" .format(generatedAddress))
		print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")

if __name__ == "__main__":
        stretchedKey = get_key()
        while True:
                try:
                        numberOfKeypairs = int(input("\n\nNumber of addresses to generate: "))
                        for generatingKeypairs in range(numberOfKeypairs):
                                generate_keypair(stretchedKey)
                                break
                except OverflowError:
                        print ("\n\nSeriously???")
                except KeyboardInterrupt:
                        exit(0)
               # except:
                        # print ("\n\nPlease try again")
