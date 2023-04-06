"""
Written by Liquid Glass

Useable functions when imported:
1. query_address()
2. query_private_key(obtainedKey)
Where obtainedKey is the password that can be obtained via PasswordUtils using get_key()

If the encrypted seed phrase (which is then converted to a private key) cannot be decrypted,
None will be passed and will continue to the next one
"""

from PasswordUtils import get_key, stretch_key
from Decrypt import decrypt_ciphertext
from globals.FilePaths import unspentUtxoPath
from algosdk import mnemonic
from base64 import b64decode
import nacl
import os

walletFile = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def query_address():
         listOfAddresses = []
         for fileList in walletFile:
                 listOfAddresses.append(open_and_read_wallet("address", fileList))
         return listOfAddresses

def query_private_key(obtainedKey):
        listOfPrivateKeys = []
        for fileList in walletFile:
                try:
                        encryptedSeedPhrase = open_and_read_wallet("seed_phrase", fileList)
                        individualSalt = open_and_read_wallet("salt", fileList)
                        stretchedKey = stretch_key(obtainedKey, individualSalt)
                        decryptedSeedPhrase = decrypt_ciphertext(encryptedSeedPhrase, stretchedKey)
                        # For testing
                        # print(decryptedSeedPhrase)
                        privateKey = mnemonic.to_private_key(decryptedSeedPhrase)
                        listOfPrivateKeys.append(privateKey)

                except nacl.exceptions.CryptoError:
                        listOfPrivateKeys.append(None)

        return listOfPrivateKeys

def open_and_read_wallet(getType, fileList):
        with open(unspentUtxoPath + fileList, "r") as currentWallet:
                searchKeywordInFile = currentWallet.readlines()
                # For testing
                # print(searchKeywordInFile)
                return find_and_obtain_type(getType, searchKeywordInFile)

def find_and_obtain_type(getType, searchKeywordInFile):
        if getType == "address":
                return obtain_address(searchKeywordInFile)
        elif getType == "seed_phrase":
                return obtain_encrypted_seed_phrase(searchKeywordInFile)
        elif getType == "salt":
                return obtain_salt(searchKeywordInFile)
        else:
                print("\n\nNo correct getType")
                exit(1)

def obtain_address(searchKeywordInFile):
        for textLines in searchKeywordInFile:
                if textLines.find("Address: ") == 0:
                        addressToList = textLines.split(": ")
                        addressWithWhitespace = addressToList[1]
                        address = addressWithWhitespace.strip()
                        return address

def obtain_encrypted_seed_phrase(searchKeywordInFile):
        for textLines in searchKeywordInFile:
                if textLines.find("Seed: ") == 0:
                        findEncryptedSeedPhrase = textLines.split(": ")
                        asciiObtainedEncryptedSeedPhrase = findEncryptedSeedPhrase[1].strip()
                        obtainedEncryptedSeedPhrase = b64decode(asciiObtainedEncryptedSeedPhrase)
                        # For testing
                        # print(obtainedEncryptedSeedPhrase)
                        return obtainedEncryptedSeedPhrase

def obtain_salt(searchKeywordInFile):
        for textLines in searchKeywordInFile:
                if textLines.find("Salt: ") == 0:
                        findSalt = textLines.split(": ")
                        asciiObtainedSalt = findSalt[1].strip()
                        obtainedSalt = b64decode(asciiObtainedSalt)
                        # For testing
                        # print(obtainedSalt)
                        return obtainedSalt

if __name__ == "__main__":
        print(walletFile)
        print(query_address())

        # Do not uncomment the 2 lines below unless needed

        # obtainedKey = get_key()
        # print(query_private_key(obtainedKey))
