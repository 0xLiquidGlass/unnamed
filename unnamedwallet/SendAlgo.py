from ValidateAddress import validate_address
from AssetBalance import query_balance_per_address
from encryption.PasswordUtils import prompt_key, stretchedKey
from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generate_keypair, generatedAddress
import AtomicTxUtils as AtomicTx

totalBalance = query_balance_per_address()*(10**6)

def prepare_send_info():
        try:
                receivingAddress = str(input("\n\nReceiver's address: "))
                validate_address(receivingAddress)
        except NotValidAddress:
                prepare_send_info()

        while True:
                print(totalBalance)
                sendingAlgos = int(input("\n\nHow many Algos to send: "))
                sendingMicroAlgos = sendingAlgos*(10**6)
                if  sendingAlgos <= totalBalance:
                        send_to_receiver("external", receivingAddress, sendingMicroAlgos)
                        break
                else:
                        print("\n\nNot enough balance. Please try again")

def send_to_receiver(receivingAddress, sendingMicroAlgos):
        prompt_key()
        AtomicTx.unsigned_tx_type_prepare("external", receivingAddress, sendingMicroAlgos)
        query_private_key(stretched_key)
        AtomicTx.prepare_sign_unsigned_tx("external", stretchedKey)
        AtomicTx.batch_unsigned_tx()
        AtomicTx.calculate_groupid()
        AtomicTx.batch_signed_tx()
        AtomicTx.send_transaction_group()
