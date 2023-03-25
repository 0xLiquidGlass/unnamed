from PasswordUtils import get_key, generate_kdf_salt, stretch_key
from Encrypt import encrypt_plaintext
from globals.FilePaths import unspentUtxoPath
from globals.Encoding import encoding
from algosdk import account, mnemonic

def generate_keypair(generatedSalt, strechedKey):
        generatedPrivateKey, generatedAddress = account.generate_account()
        with open(unspentUtxoPath+generatedAddress+".txt", "x") as newDocumentPath:
                newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
                if __name__ == "__main__":
                         print("\n\nAddress: {}" .format(generatedAddress))
                plainSeedPhrase = mnemonic.from_private_key(generatedPrivateKey)
                encryptedSeedPhrase = encrypt_plaintext(plainSeedPhrase, stretchedKey)
                newDocumentPath.write("Seed: {}\n\n".format(encryptedSeedPhrase))
                newDocumentPath.write("Salt: {}".format(generatedSalt))

if __name__ == "__main__":
        obtainedKey = get_key()
        generatedSalt = generate_kdf_salt()
        stretchedKey = stretch_key(obtainedKey, generatedSalt)
        while True:
                try:
                        numberOfKeypairs = int(input("\n\nNumber of addresses to generate: "))
                        for generatingKeypairs in range(numberOfKeypairs):
                                generate_keypair(generatedSalt, stretchedKey)
                        print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")
                        break
                except OverflowError:
                        print ("\n\nSeriously???")
                except KeyboardInterrupt:
                        exit(0)
                except FileNotFoundError:
                        print ("\n\nYour wallets directory is not created properly. Run setup and try again")
                        exit (1)
                # except:
                        # print ("\n\nPlease try again")
