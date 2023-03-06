from algosdk import account, mnemonic, constants
import os

keypairsCounted = 0
walletFile = [filename for filename in os.listdir(".") if filename.endswith(".txt")]\

def query_address():
	totalKeypairs = len(walletFile)
	currentWallet = open(walletFile, "r")
	searchKeywordInFile = currentWallet.readlines()

	for textLines in searchKeywordInFile:
		keywordIsAddress = "Line 1"
		if textLines.find(keywordIsAddress) == 0:
			# For testing 
			# print("This is a wallet")
			addressToList = textLines.split(" ")
			# For testing
			# print ("Combining address " + Address_to_list[9:67])
			address = AddressToList[9:67]
                        return address
			keypairsCounted += 1
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
                        return privateKey
			keypairsCounted += 1
	currentWallet.close()

if __name__ == "__main__":
        # Testing ground
        query_every_wallet()
        
