"""
Written by Liquid Glass
"""

from PasswordUtils import get_key, generate_kdf_salt, stretch_key
from globals.FilePaths import unspentUtxoPath, spentUtxoPath, unsafeUtxoPath
from CombineKeypairs import query_address, query_private_key
from GenerateWallet import generate_keypair
from globals.AlgodUtils import algodClient
import AtomicTxUtils as AtomicTx
import AtomicTxErrors as BalanceCheck
import os, shutil

class UtxoZeroBalance(Exception):
        pass

class UtxoUnsafeDust(Exception):
        pass

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

def consolidate_wallet_balance():
        obtainedKey = get_key()

        listOfUtxos = query_address()
        listOfPrivateKeys = query_private_key(obtainedKey)

        generatedSalt = generate_kdf_salt()
        newStretchedKey = stretch_key(obtainedKey, generatedSalt)
        receivingAddress = generate_keypair(generatedSalt, newStretchedKey)

        for currentUtxoIndex in range(len(listOfUtxos)):
                try:
                        currentUtxo = listOfUtxos[currentUtxoIndex]
                        accountInfo = algodClient.account_info(currentUtxo)
                        txFee = int(1000)
                        keepAccountAliveAmount = int(100000)
                        utxoBalance = (int(accountInfo.get("amount")) - (txFee + keepAccountAliveAmount))

                        BalanceCheck.check_valid_utxo(currentUtxo)

                        AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, utxoBalance)

                except BalanceCheck.UtxoZeroBalance:
                        continue

                except BalanceCheck.UtxoUnsafeDust:
                        currentKeypair = listOfKeypairs[currentUtxoIndex]
                        shutil.move((unspentUtxoPath + currentKeypair), unsafeUtxoPath)
                        print("The unsafe UTXO has been moved")

        AtomicTx.batch_every_unsigned_tx()

        AtomicTx.calculate_group_id()

        AtomicTx.sign_these_unsigned_txs(listOfPrivateKeys)

        AtomicTx.batch_every_signed_tx()

        AtomicTx.broadcast_atomic_txs()        

if __name__ == "__main__":
        try:
                consolidate_wallet_balance()

        except KeyboardInterrupt:
                exit(0)
