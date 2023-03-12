from algosdk import account
from CombineKeypairs import query_address
from AlgodUtils import algodClient

def query_balance_per_address():
	totalBalanceInMicroAlgos = 0
	for individualAddress in query_address():
		# For testing
		# print(individualAddress)
		# print(algodClient)
		accountInfo = algodClient.account_info(individualAddress)
		totalBalanceInMicroAlgos += accountInfo.get("amount")
	print ("Your Balance: {:.2f} Algos" . format(totalBalanceInMicroAlgos*(10**-6)))	


if __name__ == "__main__":
	query_balance_per_address()
