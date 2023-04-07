"""
Written by Liquid Glass

Useable functions when imported:

1. import_and_sweep()

This function allows the user to import their old seed phrase (from another wallet)
and sweep the balance to a newly generated UTXO
"""

from GenerateWallet import generate_keypair
from PasswordUtils import get_key_for_encryption, generate_kdf_salt, stretch_key
from WalletMovements import remove_change_wallet
import NormalTxUtils as NormalTx
from globals.AlgodUtils import algodClient
from globals.ValueConstants import txFeeConst
from globals.FilePaths import unspentUtxoPath
from algosdk import mnemonic, accounts, transaction
import algosdk
import os

listSweepToUtxoAddress = []

txFee = txFeeConst

def import_and_sweep():
        try:
                userInputSeedPhrase = str(input("\n\nInput your seed phrase: "))

                sweepAddressPrivateKey = obtain_private_key(userInputSeedPhrase)

                sweepAddress = obtain_address_from_private_key(sweepAddressPrivateKey)

                sweepAmount = get_sweep_amount(sweepAddress)

                sweep_old_wallet(sweepAddress, sweepAmount, sweepAddressPrivateKey)

        except algosdk.error.InvalidSecretKeyError as algosdkErrorMessage:
                print("\n{}" . format(algosdkErrorMessage))
                print("\nPlease try again")

                import_and_sweep()

        except:
                print("\n\nThe sending process was interrupted")
                sweepToUtxoAddress = listSweepToUtxoAddress[0]
                sweepToUtxoAddressInfo = algodClient.account_info(sweepToUtxoAddress)
                sweepToUtxoAddressBalance = sweepToUtxoAddressInfo.get("amount")

                remove_unused_generated_utxo(sweepToUtxoAddress, sweepToUtxoAddressBalance)

                exit(1)

def remove_unused_generated_utxo(sweepToUtxoAddress, sweepToUtxoAddressBalance):
        if sweepToUtxoAddressBalance > float(0):
                os.remove(unspentUtxoPath + sweepToUtxoAddress + ".txt")

def obtain_private_key(userInputSeedPhrase):
        userPrivateKeyFromSeedPhrase = mnemonic.to_private_key(userInputSeedPhrase)
        return userPrivateKeyFromSeedPhrase

def obtain_address_from_private_key(sweepAddressPrivateKey):
        obtainedSweepAddress = account.address_from_private_key(userPrivateKey)
        return obtainedSweepAddress

def get_sweep_amount(sweepAddress):
        sweepAccountInfo = algodClient.account_info(sweepAddress)
        sweepAccountBalance = sweepAccountInfo.get("amount")
        sweepAccountSendBalance = sweepAccountBalance - txFee
        return sweepAccountSendBalance

def sweep_old_wallet(sweepAddress, sweepAmount, sweepAddressPrivateKey):
        obtainedKey = get_key_for_encryption()
        generatedSalt = generate_kdf_salt()
        stretchedKey = stretch_key(obtainedKey, generatedSalt)

        generatedAddress = generate_keypair(generatedSalt, stretchedKey)

        listSweepToUtxoAddress.append(generatedAddress)

        unsignedSweepTx = NormalTx.initiate_unsigned_normal_tx(sweepAddress, generatedAddress
                                                               , sweepAmount, generatedAddress)

        signedSweepTx = NormalTx.sign_unsigned_normal_tx(unsignedSweepTx, sweepAddressPrivateKey)

        broascast_signed_normal_tx(signedSweepTx)

if __name__ == "__main__":
        import_and_sweep()
