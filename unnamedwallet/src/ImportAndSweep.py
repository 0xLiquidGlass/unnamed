"""
Written by Liquid Glass

Useable functions when imported:

1. import_and_sweep()

This function allows the user to import their old seed phrase (from another wallet)
and sweep the balance to a newly generated UTXO
"""

from GenerateWallet import generate_keypair
from PasswordUtils import get_key_for_encryption, generate_kdf_salt, stretch_key
import NormalTxUtils as NormalTx
from globals.AlgodUtils import algodClient
from globals.ValueConstants import txFeeConst
from globals.FilePaths import unspentUtxoPath
from algosdk import mnemonic, account, transaction
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

        except algosdk.error.WrongMnemonicLengthError as mnemonicLengthErrorMessage:
                print("\n{}" .format(mnemonicLengthErrorMessage))
                print("\nPlease try again")

                import_and_sweep()

        except algosdk.error.WrongAmountType:
                print("\n\nThe sending process was interrupted")
                print("\nMake sure that your account that you want to sweep has balance")
                sweepToUtxoAddress = listSweepToUtxoAddress[0]
                sweepToUtxoAddressInfo = algodClient.account_info(sweepToUtxoAddress)
                sweepToUtxoAddressBalance = sweepToUtxoAddressInfo.get("amount")

                remove_unused_generated_utxo(sweepToUtxoAddress, sweepToUtxoAddressBalance)

                exit(1)

        except KeyboardInterrupt:
                print("\n\nThe sending process was interrupted")
                if len(listSweepToUtxoAddress) > int(0):
                        sweepToUtxoAddress = listSweepToUtxoAddress[0]
                        sweepToUtxoAddressInfo = algodClient.account_info(sweepToUtxoAddress)
                        sweepToUtxoAddressBalance = sweepToUtxoAddressInfo.get("amount")

                        remove_unused_generated_utxo(sweepToUtxoAddress, sweepToUtxoAddressBalance)

                        exit(0)

        except:
                print("\n\nThe sending process was interrupted")
                print("\nCheck if your seed phrase was entered correctly")
                if len(listSweepToUtxoAddress) > int(0):
                        sweepToUtxoAddress = listSweepToUtxoAddress[0]
                        sweepToUtxoAddressInfo = algodClient.account_info(sweepToUtxoAddress)
                        sweepToUtxoAddressBalance = sweepToUtxoAddressInfo.get("amount")

                        remove_unused_generated_utxo(sweepToUtxoAddress, sweepToUtxoAddressBalance)

                exit(1)

def remove_unused_generated_utxo(sweepToUtxoAddress, sweepToUtxoAddressBalance):
        if sweepToUtxoAddressBalance == float(0):
                os.remove(unspentUtxoPath + sweepToUtxoAddress + ".txt")

def obtain_private_key(userInputSeedPhrase):
        userPrivateKeyFromSeedPhrase = mnemonic.to_private_key(userInputSeedPhrase)
        return userPrivateKeyFromSeedPhrase

def obtain_address_from_private_key(sweepAddressPrivateKey):
        obtainedSweepAddress = account.address_from_private_key(sweepAddressPrivateKey)
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

        NormalTx.broadcast_signed_normal_tx(signedSweepTx)

if __name__ == "__main__":
        print("As of v1.0.0, support for ASAs are not yet available") 
        print("\nDo not sweep accounts with ASAs in them")
        print("\nAttemping to sweep accounts with ASAs can result in your ASAs not being visible in the wallet")
        import_and_sweep()
