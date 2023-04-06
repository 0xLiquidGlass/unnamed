"""
Written by Liquid Glass

Useable functions when imported:

1. prompt_send_algos()

This function allows you to manually input the amount you want to spend and the
the address that will receive the specified amount of Algos. Removes whitespace
when pasting receiving address

An interface for prepare_send_algos(sendAmountMicroAlgos, receivingAddress)

2. prepare_send_algos(sendAmountMicroAlgos, receivingAddress)

This function will check every individual address in the unspent/ directory for
a valid balance (i.e. a positive balance and no dust balance), whether to send the
full balance to the recipient or partially (where the final balance which will
fulfil the specified amount to send with the leftovers, also known as change, will
go to a change address which is a newly generated address that you own)

Only needs the send amount (in microAlgos) and the receiving address
which the sent amount will go to to be passed to this function
"""

from PasswordUtils import get_key, generate_kdf_salt, stretch_key
from globals.FilePaths import unspentUtxoPath, spentUtxoPath, unsafeUtxoPath
from globals.ValueConstants import txFeeConst
from AssetBalance import query_balance_per_address
from GenerateWallet import generate_keypair
from CombineKeypairs import query_address, query_private_key
from ValidateAddress import validate_address
from globals.AlgodUtils import algodClient
import WalletMovementUtils as WalletMovement
import NormalTxUtils as NormalTx
import AtomicTxUtils as AtomicTx
import AtomicTxErrors as BalanceCheck
import os, shutil

listOfKeypairs = [filename for filename in os.listdir(unspentUtxoPath) if filename.endswith(".txt")]\

listChangeAddress = []
listMovedKeypairs = []

# Sensitive data, private keys involved
listRelevantPrivateKeys = []

countFrom = int(0)

txFee = txFeeConst

def prompt_send_algos():
        try:
                totalWalletBalanceMicroAlgos = query_balance_per_address()
                totalWalletBalanceAlgos = totalWalletBalanceMicroAlgos * (10 ** -6)
                print("In microAlgos: {}\n".format(totalWalletBalanceMicroAlgos))
                sendAmount = float(input("\nHow many Algos to send: "))
                sendAmountMicroAlgos = int(sendAmount * (10 ** 6))
                # For testing
                # print(sendAmountMicroAlgos)

                if sendAmountMicroAlgos < int(0):
                        print("\nNo negative numbers. Positive numbers only")
                        print("\nPlease try again")
                        prompt_send_algos()

                elif sendAmountMicroAlgos == int(0):
                        print("\n")
                        prompt_send_algos()

                elif sendAmountMicroAlgos <= totalWalletBalanceMicroAlgos:
                        receivingAddress = str(input("\nReceiving Address: "))
                        receivingAddressNoWhitespace = receivingAddress.strip()
                        addressErrorCodes = validate_address(receivingAddressNoWhitespace)
                        if addressErrorCodes == int(1):
                                print("\nThis address is not valid")
                                print("\nPlease try again")
                                prompt_send_algos()

                        else:
                                prepare_send_algos(sendAmountMicroAlgos, receivingAddressNoWhitespace)

                else:
                        print("\nYou do not have enough balance in your wallet")
                        print("\nPlease try again with a different amount")
                        prompt_send_algos()

        except ValueError:
                print("\nPlease try again")
                prompt_send_algos()

        except TypeError:
                print("\nPlease try again")
                prompt_send_algos()

def prepare_send_algos(sendAmountMicroAlgos, receivingAddress):
        amountLeft = sendAmountMicroAlgos
        amountToSend = sendAmountMicroAlgos

        obtainedKey = get_key()

        listOfUtxos = query_address()

        # Sensitive data, private keys involved
        listOfPrivateKeys = query_private_key(obtainedKey)

        countUpTo = len(listOfUtxos)
        countIncrement = int(1)

        for currentUtxoIndex in range(countFrom, countUpTo, countIncrement):
                currentUtxo = listOfUtxos[currentUtxoIndex]
                accountInfo = algodClient.account_info(currentUtxo)
                currentBalance = (int(accountInfo.get("amount")) - txFee)

                localErrorCodeReturned = BalanceCheck.check_valid_utxo(currentUtxo)

                if localErrorCodeReturned == int(0):
                        changeSwitch = check_utxo_for_change_tx(amountLeft, currentBalance)

                        unsignedNormalTx = tx_with_no_change(changeSwitch, currentUtxo
                                                             , receivingAddress, currentBalance)

                        tx_with_change(changeSwitch, obtainedKey, currentUtxo, receivingAddress
                                       , amountLeft, currentBalance)

                        amountLeft = amountLeft - currentBalance

                        prepare_private_keys(changeSwitch, currentUtxoIndex, listOfPrivateKeys)

                elif localErrorCodeReturned == int(1):
                        continue

                elif localErrorCodeReturned == int(2):
                        WalletMovement.move_utxo_to_unsafe_dir(currentUtxoIndex)

                if amountLeft <= float(0):
                        break

        execute_send_algos(unsignedNormalTx)

def check_utxo_for_change_tx(amountLeft, currentBalance):
        if amountLeft >= currentBalance:
                # For testing
                # print("No change")
                return int(0)

        else:
                # For testing
                # print("Change")
                return int(1)

def tx_with_no_change(changeSwitch, currentUtxo, receivingAddress, currentBalance):
        if changeSwitch == int(0):
              AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, currentBalance
                                            , receivingAddress)

              unsignedNormalTx = NormalTx.initiate_unsigned_normal_tx(currentUtxo, receivingAddress
                                                                , currentBalance, receivingAddress)

              return unsignedNormalTx

def tx_with_change(changeSwitch, obtainedKey, currentUtxo
                   , receivingAddress, amountLeft, currentBalance):
        if changeSwitch == int(1):
                receivingAmount = amountLeft

                generatedSalt = generate_kdf_salt()

                stretchedKey = stretch_key(obtainedKey, generatedSalt)

                changeAddress = generate_keypair(generatedSalt, stretchedKey)

                listChangeAddress.append(changeAddress)

                changeAmount = currentBalance - receivingAmount - txFee

                AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, receivingAmount
                                              , None)

                AtomicTx.initiate_unsigned_tx(currentUtxo, changeAddress, changeAmount
                                              , changeAddress)

def prepare_private_keys(changeSwitch, currentUtxoIndex, listOfPrivateKeys):
        currentPrivateKey = listOfPrivateKeys[currentUtxoIndex]
        if currentPrivateKey == None:
                print("\nThe private key for {} cannot be decrypted" .format(currentUtxo))
                print("\nMoving on to the next one")
                return

        if changeSwitch == int(0):
                listRelevantPrivateKeys.append(currentPrivateKey)
                WalletMovement.move_utxo_to_spent_dir(currentUtxoIndex)

        elif changeSwitch == int(1):
                countUpTo = int(2)
                countIncrement = int(1)
                for txPrivateKeyIndex in range(countFrom, countUpTo, countIncrement):
                        listRelevantPrivateKeys.append(currentPrivateKey)
                WalletMovement.move_utxo_to_spent_dir(currentUtxoIndex)

def execute_send_algos(unsignedNormalTx):
        numberOfAtomicTransactions = len(AtomicTx.listUnsignedTx)
        if numberOfAtomicTransactions == int(1):
                AtomicTx.listUnsignedTx.clear()

                correspondingPrivateKey = listRelevantPrivateKeys[0]

                signedNormalTx = NormalTx.sign_unsigned_normal_tx(unsignedNormalTx
                                                                  , correspondingPrivateKey)

                NormalTx.broadcast_signed_normal_tx(signedNormalTx)

        elif numberOfAtomicTransactions > int(1):
                del unsignedNormalTx

                AtomicTx.batch_every_unsigned_tx()

                AtomicTx.calculate_group_id()

                AtomicTx.sign_these_unsigned_txs(listRelevantPrivateKeys)

                AtomicTx.batch_every_signed_tx()

                AtomicTx.broadcast_atomic_txs()

if __name__ == "__main__":
        try:
                if len(listOfKeypairs) == int(0):
                        print("\nYou do not have any UTXOs yet")
                        print("\nMake a new UTXO and fund it before spending")
                        exit(0)
                        
                else:
                        prompt_send_algos()

        except:
                WalletMovement.revert_moved_utxo(listMovedKeypairs, listChangeAddress)
