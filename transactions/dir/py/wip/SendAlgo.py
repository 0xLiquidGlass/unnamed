from ValidateAddress import validate_address
from AssetBalance import query_balance_per_address
from encryption.PasswordUtils import prompt_key, stretchedKey
from CombineKeypairs import query_address, query_private_key
from globals.FilePaths import unspentUtxoPath, spentUtxoPath, unsafeUtxoPath
from GenerateWallet import generate_keypair, generatedAddress
from globals.AlgodUtils import algodClient
from algosdk import transaction
import os, shutil

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

listUnsignedTx = []
batchedUnsignedTx = []
listSignedTx = []
batchedSignedTx = []
params = algodClient.suggested_params()

def prompt_send_info():
	query_balance_per_address()
	sendAmount = int(input("\n\nAmount of Algos to send:"))
	prompt_address_validate()

	if validate_address() == True:
		prepare_tx_info(sendAmount, sendAddress)
	else:
		prompt_send_info()

def prompt_address_validate():
        while True:
                try:
                        sendAddress = str(input("\n\nReceiver's address: "))
                        validate_address(sendAddress)
                        break

                except:
                        print("\n\nPlease try agian")

                except KeyboardInterrupt:
                        exit()

def prepare_tx_info(sendAmount, sendAddress):
	for remainingUtxos in range(len(listOfKeypairs)):
		currentUtxo = query_address()[remainingUtxos]
		currentUtxoInfo = algodClient.account_info(currentUtxo)
		currentUtxoBalance = currentUtxoInfo.get("amount")

		try:
			validate_utxo_requirements(currentUtxoBalance)
	                decide_utxo_send_amount(sendAddress, currentUtxoBalance, sendAmount)
		except ZeroBalanceError:
			pass
		except UnsafeDustBalance:
			shutil.move(listOfKeypairs[remainingUtxos], unsafeUtxoPath)

def validate_utxo_requirements(currentUtxoBalance):
	if currentUtxoBalance > int(0):
		check_for_dust(currentUtxoBalance)
	else:
		raise ZeroBalanceError

def check_for_dust(currentUtxoBalance):
	if currentUtxoBalance >= int(10**4):
		pass
	else:
		raise UnsafeDustBalance

def decide_utxo_send_amount(sendAddress, currentUtxoBalance, sendAmount):
	if (sendAmount - currentUtxoBalance) >= sendAmount:
		prepare_unsigned_tx(currentUtxo, params, sendAddress, currentUtxoBalance)
	else:
		spendingAmount = currentUtxoBalance - sendAmount
		changeAmount = currentUtxoBalance - spendingAmount
		prepare_unsigned_tx(currentUtxo, params, sendAddress, spendingAmount)
                prepare_change(currentUtxo, params, changeAmount)

def prepare_change(currentUtxo, params, changeAmount):
        prompt_key()
        generate_keypair(stretchedKey)
        
        prepare_unsigned_tx(currentUtxo, params, sendAddress, changeAmount)

def prepare_unsigned_tx(currentUtxo, params, sendAddress, spendingAmount):
        # Sensitive data, contains seed phrase and private keys
	query_private_key(stretchedKey)
        unsignedTx = transaction.PaymentTxn(currentUtxo, params, sendAddress, spendingAmount)
        listUnsignedTx.append(unsignedTx)
        batch_unsigned_tx()
        calculate_groupid()
        prepare_signed_tx()

def batch_unsigned_tx():
       	for batchingListTxInfo in range(0, len(listUnsignedTx), 16):
	        batchingUnsignedTx = listUnsignedTx[batchingListTxInfo:batchingListTxInfo + 16]
	        batchedUnsignedTx.append(batchingUnsignedTx)

def calculate_groupid():
	for txBatches in range(len(batchedUnsignedTx)):
		groupId = transaction.calculate_group_id(batchedUnsignedTx[txBatches])
	for countUnsignedTx in range(len(listUnsignedTx)):
		listUnsignedTx[countUnsignedTx] = groupId

# Private keys involved
def prepare_signed_tx():
        for signingUnsignedTx in range(len(listUnsignedTx)):
                signedTx = 

def batch_signed_tx():
        
