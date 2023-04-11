from PasswordUtils import get_key_for_encryption, generate_kdf_salt, stretch_key
from Encrypt import encrypt_plaintext
from globals.Encoding import textEncodingFormat
from globals.FilePaths import asaUnspentUtxoPath
from algosdk import account, mnemonic
from base64 import b64encode

def generate_asa_keypair(assetId, generatedSalt, stretchedKey):
        generatedPrivateKey, generatedAddress = account.generate_account()
        with open(asaUnspentUtxoPath + generatedAddress + ".txt", "x") as newDocumentPath:
                newDocumentPath.write("Asset ID: {}\n\n" .format(assetId))
                newDocumentPath.write("Address: {}\n\n" .format(generatedAddress))
                plainSeedPhrase = mnemonic.from_private_key(generatedPrivateKey)
                encryptedSeedPhrase = encrypt_plaintext(plainSeedPhrase, stretchedKey)
                b64encodedEncryptedSeedPhrase = b64encode(encryptedSeedPhrase)
                b64encodedGeneratedSalt = b64encode(generatedSalt)
                stringEncryptedSeedPhrase = b64encodedEncryptedSeedPhrase.decode(textEncodingFormat)
                stringGeneratedSalt = b64encodedGeneratedSalt.decode(textEncodingFormat)
                newDocumentPath.write("Seed: {}\n\n".format(stringEncryptedSeedPhrase))
                newDocumentPath.write("Salt: {}".format(stringGeneratedSalt))
                return generatedAddress

if __name__ == "__main__":
        print("What type of account do you want to generate?")
        print("\n\n1 --> Dapps")
        keyGenerationType = str(input("\n\nYour choice:"))
        if keyGenerationType == str(1):
                None
