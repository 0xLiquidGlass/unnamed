"""
To do:
1. Make print() iterate once
2. Test and modify
"""

from algosdk import account
from CombineKeypairs import query_address, walletFile
from AlgodUtils import algodClient

totalKeypairs = len(walletFile)
keypairsCounted = 0

def query_balance_per_address():
	# For testing
	# print(query_address())
	# print(algodClient)
	totalBalanceInMicroAlgos = 0
	accountInfo = algodClient.account_info(query_address())
	totalBalanceInMicroAlgos += accountInfo.get("amount")
	print ("Your Balance: {:.2f} Algos" . format(totalBalanceInMicroAlgos*(10**-6)))	

for keypairsCounted in walletFile:
	# For testing	
	# print ("ok")
	query_balance_per_address()