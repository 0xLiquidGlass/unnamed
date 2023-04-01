"""
Written by Liquid Glass

Useable functions when imported:

1. query_unused_utxos()

Displays all UTXOs with exactly 0 balance. However, it does not check if the UTXO has been spent or not
"""

from globals.FilePaths import unspentUtxoPath
from globals.AlgodUtils import algodClient
from CombineKeypairs import query_address
import os

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def list_unused_utxos():
        for currentUtxoIndex in range(len(listOfKeypairs)):
                currentAddress = (query_address()[currentUtxoIndex])
                currentUtxoInfo = algodClient.account_info(currentAddress)
                balanceInMicroAlgos = currentUtxoInfo.get("amount")
                # For testing
                # print(balanceInMicroAlgos)
                if balanceInMicroAlgos == int(0):
                        displayCurrentUtxo = (currentAddress)
                        print("\n{}\n".format(displayCurrentUtxo))
                else:
                        pass

def query_unused_utxos():
        if len(listOfKeypairs) > int(0):
                list_unused_utxos()
        else:
                print("\n\nYou do not have any unused UTXOs yet")
                print("\n\nPlease create a new UTXO\n\n")

if __name__ == "__main__":
        query_unused_utxos()
