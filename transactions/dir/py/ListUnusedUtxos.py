from globals.AlgodUtils import algodClient
from CombineKeypairs import query_address
import os

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\


def list_unused_utxos():
	for currentUtxoIndex in range(len(listOfKeypairs)):
		currentUtxoInfo = algodClient.account_info(listOfKeypairs[currentUtxoIndex])
		balanceInMicroAlgos = currentUtxoInfo.get("amount")
		if balanceInMicroAlgos != int(0):
			print (("\n\n" + currentUtxoIndex + 1) + ". " + listOfKeypairs[currentUtxoIndex])
		else:
			pass

def query_unused_utxos():
	if len(listOfKeypairs) != len(0):
		list_unused_utxos()
	else:
		print ("\n\nYou do not have any unused UTXOs yet")
		print ("\n\nPlease create a new UTXO")

if __name__ == "__main__":
	query_unused_utxos()
