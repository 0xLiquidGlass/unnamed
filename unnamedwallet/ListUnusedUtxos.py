"""
Written by Liquid Glass

Useable functions when imported:

1. query_unused_utxos()

Displays all UTXOs with 0 balance. However, it does not check if the UTXO has been spent or not
"""

from globals.AlgodUtils import algodClient
from CombineKeypairs import query_address
import os

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def list_unused_utxos():
	for currentUtxoIndex in range(len(listOfKeypairs)):
		currentUtxoInfo = algodClient.account_info(listOfKeypairs[currentUtxoIndex])
		balanceInMicroAlgos = currentUtxoInfo.get("amount")
		if balanceInMicroAlgos = int(0):
                        displayCurrentIndex = (currentUtxoIndex + 1)
                        displayCurrentUtxo = (listOfKeypairs[currentUtxoIndex])
			print("\n\n" + displayCurrentIndex + ". " + displayCurrentUtxo)
		else:
			pass

def query_unused_utxos():
	if len(listOfKeypairs) > len(0):
		list_unused_utxos()
	else:
		print("\n\nYou do not have any unused UTXOs yet")
		print("\n\nPlease create a new UTXO")

if __name__ == "__main__":
	query_unused_utxos()
