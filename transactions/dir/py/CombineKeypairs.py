"""
To do:
1. Modify and cleanup query_private_key
2. Handle more than 2 iterations
3. Test program
"""

from algosdk import mnemonic
import os

walletFile = [filename for filename in os.listdir("../wallet") if filename.endswith(".txt")]\

def query_address():
	for fileList in walletFile:
		currentWallet = open("../wallet/"+fileList, "r")
		searchKeywordInFile = currentWallet.readlines()
		for textLines in searchKeywordInFile:
			if textLines.find("Address") == 0:
				# For testing 
				# print("This is a wallet")
				addressToList = textLines.split(" ")
				# For testing
				# print (addressToList[1])
				address = addressToList[1]
				return address
		currentWallet.close()

def query_private_key():
	totalKeypairs = len(walletFile)
	currentWallet = open(walletFile, "r")
	searchKeywordInFile = currentWallet.readlines()
	for textLines in searchKeywordInFile:
		keywordIsSeed = "Line 3"
		if textLines.find(keywordIsSeed) == 0:
			# For testing
			# print("This is a wallet")
			seedToList = textLines.split(" ")
			# For testing
			# print ("Showing Seed Phrase: " + Seed_to_list[1:26])
			seedPhrase = seedToList[1:26]
			mnemonic.to_private_key(seedPhrase)
			keypairsCounted += 1
			return privateKey
	currentWallet.close()

if __name__ == "__main__":
	print(query_address())