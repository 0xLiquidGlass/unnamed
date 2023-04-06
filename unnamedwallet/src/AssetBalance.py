"""
Written by Liquid Glass

Useable functions when imported:

1. query_balance_per_address()

Where this function sums up all of the assets in every UTXO and then shows the total balance

Returns the whole wallet's balance in microAlgos when the query_balance_per_address() function is called and used as output
"""

from algosdk import account
from CombineKeypairs import query_address, query_private_key
from globals.AlgodUtils import algodClient

def query_balance_per_address():
        totalBalanceInMicroAlgos = int(0)
        for individualAddress in query_address():
		# For testing
		# print(individualAddress)
		# print(algodClient)
                accountInfo = algodClient.account_info(individualAddress)
                totalBalanceInMicroAlgos += accountInfo.get("amount")
        print ("\n\nYour Balance: {:.2f} Algos\n\n" . format(totalBalanceInMicroAlgos*(10**-6)))
        return totalBalanceInMicroAlgos


if __name__ == "__main__":
        query_balance_per_address()
