"""
Written by Liquid Glass

Useable functions when imported:
1. query_address()
2. query_private_key(obtainedKey)
Where obtainedKey is the password that can be obtained via PasswordUtils using get_key()
"""

from PasswordUtils import get_key, stretch_key
from Decrypt import decrypt_ciphertext
from globals.FilePaths import unspentUtxoPath
from globals.Encoding import naclEncodingFormat
from algosdk import mnemonic, encoding
import os

walletFile = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def query_address():
         listOfAddresses = []
         listOfAddresses.append(open_and_read_wallet("address"))
         return listOfAddresses

def query_private_key(obtainedKey):
        listOfPrivateKeys = []
        encryptedSeedPhrase = open_and_read_wallet("seed_phrase")
        # For testing
        # print(encryptedSeedPhrase)
        individualSalt = open_and_read_wallet("salt")
        # For testing
        # print(individualSalt)
        stretchedKey = stretch_key(obtainedKey, individualSalt)
        decryptedSeedPhrase =  decrypt_ciphertext(encryptedSeedPhrase, stretchedKey)
        # For testing
        # print(decryptedSeedPhrase)
        privateKey = mnemonic.to_private_key(decryptedSeedPhrase)
        listOfPrivateKeys.append(privateKey)
        return listOfPrivateKeys

def open_and_read_wallet(getType):
        for fileList in walletFile:
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
                        obtainedEncryptedSeedPhrase = findEncryptedSeedPhrase[1].strip()
                        # For testing
                        # print(obtainedEncryptedSeedPhrase)
                        return obtainedEncryptedSeedPhrase.encode(naclEncodingFormat)

def obtain_salt(searchKeywordInFile):
        for textLines in searchKeywordInFile:
                if textLines.find("Salt: ") == 0:
                        findSalt = textLines.split(": ")
                        obtainedSalt = findSalt[1].strip()
                        # For testing
                        # print(obtainedSalt)
                        return obtainedSalt.encode(naclEncodingFormat)

if __name__ == "__main__":
        print(walletFile)
        print(query_address())
        obtainedKey = get_key()
        print(query_private_key(obtainedKey))
