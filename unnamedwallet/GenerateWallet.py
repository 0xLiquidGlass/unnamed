from PasswordUtils import get_key
from Encrypt import encrypt_plaintext
from globals.FilePaths import unspentUtxoPath
from globals.Encoding import encoding
from algosdk import account, mnemonic

generatedPrivateKey, generatedAddress = account.generate_account()

def generate_keypair(stretchedKey):
        with open(unspentUtxoPath+generatedAddress+".txt", "x") as newDocumentPath:
                newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
                plainSeedPhrase = mnemonic.from_private_key(generatedPrivateKey)
                encryptedSeedPhrase = encrypt_plaintext(plainSeedPhrase, stretchedKey)
                newDocumentPath.write("Seed: {}".format(encryptedSeedPhrase))

if __name__ == "__main__":
        stretchedKey = get_key()
        while True:
                try:
                        numberOfKeypairs = int(input("\n\nNumber of addresses to generate: "))
                        for generatingKeypairs in range(numberOfKeypairs):
                                generate_keypair(stretchedKey)
                                break
                        print("\n\nAddress: {}" .format(generatedAddress))
                        print("\n\nPlease Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!\n\n")
                        break
                except OverflowError:
                        print ("\n\nSeriously???")
                except KeyboardInterrupt:
                        exit(0)
                except FileNotFoundError:
                        print ("Your wallets directory is not created properly. Run setup and try again")
                        exit (1)
                # except:
                        # print ("\n\nPlease try again")
