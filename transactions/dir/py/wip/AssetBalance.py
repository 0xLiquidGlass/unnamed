from algosdk import account, mnemonic
from algosdk.v2client import algod
import CombineKeypairs

totalBalanceInMicroalgos = 0
algodAddress = ""
algodToken = ""
algodClient = algod.AlgodClient(algodToken, algodAddress)

def query_balance_per_address():
	accountInfo = algodclient.account_info(CombineKeypairs.query_every_wallet())
	totalBalanceInMicroalgos += acccountInfo.get("amount")

def show_total_balance():
	print ("Your Balance: {:.2f} Algos" . format(totalBalanceInMicroalgos*(10**-6)))

while (keypairsCounted <= totalKeypairs):
	queryBalancePerAddresss()

if __name__ == "__main__":
        showTotalBalance()
