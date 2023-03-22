"""
To do:
1. Handle more than 2 iterations, can handle 2 currently
2. Test program and simulate with balance
"""
from PasswordUtils import get_key
from Decrypt import decrypt_ciphertext
from globals.FilePaths import unspentUtxoPath
from algosdk import mnemonic, encoding
import os

walletFile = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def query_address():
	listOfAddresses = []
	for fileList in walletFile:
		with open(unspentUtxoPath+fileList, "r") as currentWallet:
		        searchKeywordInFile = currentWallet.readlines()
		        for textLines in searchKeywordInFile:
			        if textLines.find("Address") == 0:
				        # For testing
				        # print("This is a wallet")
				        addressToList = textLines.split(" ")
				        # For testing
				        # print (addressToList[1])
				        addressWithWhitespace = addressToList[1]
				        address = addressWithWhitespace.strip()
				        listOfAddresses.append(address)
	return listOfAddresses

def query_private_key(stretchedKey):
	listOfPrivateKeys = []
	for fileList in walletFile:
		with open(unspentUtxoPath+fileList, "r") as currentWallet:
		        searchKeywordInFile = currentWallet.readlines()
		        for textLines in searchKeywordInFile:
			        if textLines.find("Seed") == 0:
				        # For testing
				        # print("This is a wallet")
				        encryptedSeedPhrase = textLines.split(" ")
				        # For testing
				        # print (individualWords[1])
				        decryptedSeedPhrase = decrypt_ciphertext(encryptedSeedPhrase[0], stretchedKey)
				        privateKey = mnemonic.to_private_key(decryptedSeedPhrase)
				        listOfPrivateKeys.append(privateKey)
	return listOfPrivateKeys

if __name__ == "__main__":
	print(walletFile)
	print(query_address())
	print(query_private_key(get_key()))
