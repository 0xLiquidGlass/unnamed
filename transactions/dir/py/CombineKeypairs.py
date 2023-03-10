"""
To do:
1. Handle more than 2 iterations, can handle 2 currently
2. Test program and simulate with balance
"""

from algosdk import mnemonic, encoding
import os

walletFile = [filename for filename in os.listdir("../wallet/transaction/unspent/") if filename.endswith(".txt")]\

def query_address():
	listOfAddresses = []
	for fileList in walletFile:
		currentWallet = open("../wallet/transaction/unspent/"+fileList, "r")
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
		currentWallet.close()
	return listOfAddresses

def query_private_key():
	listOfPrivateKeys = []
	for fileList in walletFile:
		currentWallet = open("../wallet/transaction/unspent/"+fileList, "r")
		searchKeywordInFile = currentWallet.readlines()
		for textLines in searchKeywordInFile:
			if textLines.find("Seed") == 0:
				# For testing
				# print("This is a wallet")
				individualWords = textLines.split(" ")
				# For testing
				# print (individualWords[1:26])
				seedPhrase = " ".join(individualWords[1:26])
				privateKey = mnemonic.to_private_key(seedPhrase)
				listOfPrivateKeys.append(privateKey)
		currentWallet.close()
	return listOfPrivateKeys

if __name__ == "__main__":
	print(walletFile)
	print(query_address())
	print(query_private_key())