"""
Documentation of atomic transaction:
https://developer.algorand.org/docs/get-details/atomic_transfers/

Documentation of Algorand Python SDK:
1. https://developer.algorand.org/docs/sdks/python/
2. https://py-algorand-sdk.readthedocs.io/en/latest/
"""

from encryption.PasswordUtils import prompt_key, stretchedKey
from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generatedAddress, generate_keypair
import AtomicTxUtils as AtomicTx

def consolidate_balance():
	prompt_key()
        generate_keypair(stretchedKey)
        receivingAddress = generatedAddress
        AtomicTx.unsigned_tx_type_prepare("internal", receivingAddress, None)
        query_private_key(stretchedKey)
        AtomicTx.prepare_sign_unsigned_tx("internal", stretchedKey)
        AtomicTx.batch_unsigned_tx()
        AtomicTx.calculate_groupid()
        AtomicTx.batch_signed_tx()
        AtomicTx.send_transaction_group()

if __name__ == "__main__":
        consolidate_balance()
