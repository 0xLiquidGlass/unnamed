"""
Written by Liquid Glass
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
                        addressErrorCodes = validate_address(receivingAddress)
                        if addressErrorCodes == int(1):
                                print("\nThis address is not valid")
                                print("\nPlease try again")
                                prompt_send_algos()

                        else:
                                prepare_send_algos(sendAmountMicroAlgos, receivingAddress)

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

        obtainedKey = getKey()

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
                        changeSwitch = check_utxo_for_change_tx(amountLeft, amountToSend)

                        unsignedNormalTx = tx_with_no_change(changeSwitch, currentUtxo
                                                             , receivingAddress, currentBalance
                                                             , receivingAddress)

                        tx_with_change(changeSwitch, currentUtxo, receivingAddress
                                       , amountLeft, currentBalance, receivingAddress)

                        amountLeft = amountLeft - utxoBalance

                        prepare_private_keys(changeSwitch, currentUtxoIndex, listOfPrivateKeys)

                elif localErrorCodeReturned == int(1):
                        continue

                elif localErrorCodeReturned == int(2):
                        WalletMovement.move_utxo_to_unsafe_dir(currentUtxoIndex)

                if amountLeft == float(0):
                        break

        execute_send_algos(unsignedNormalTx)

def check_utxo_for_change_tx(amountLeft, amountToSend):
        if amountLeft >= amountToSend:
                return int(0)

        else:
                return int(1)

def tx_with_no_change(changeSwitch, currentUtxo, receivingAddress, currrentBalance, receivingAddress):
        if changeSwitch == int(0):
              AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, currentBalance
                                            , receivingAddress)

              unsignedNormalTx = NormalTx.initiate_unsigned_normal_tx(currentUtxo, receivingAddress
                                                                , currentBalance, receivingAddress)

              return unsignedNormalTx

def tx_with_change(changeSwitch, currentUtxo, receivingAddress
                   , amountLeft, currrentBalance, receivingAddress):
        if changeSwitch == int(1):
                sendAmount = amountLeft
                changeAmount = currentBalance - sendAmount

                AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, sendAmount, None)

                AtomicTx.initiate_unsigned_tx(currentUtxo, receivingAddress, changeAmount
                                              , receivingAddress)

def prepare_private_keys(changeSwitch, currentUtxoIndex, listOfPrivateKeys):
        currentPrivateKey = listOfPrivateKeys[currentUtxoIndex]
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

def revert_moved_utxo():
        WalletMovement.unmove_spent_utxos(listMovedKeypairs)

        print("\n\nThe process has been interrupted")
        print("\nMoving all spent UTXOs back to unspent")
        exit(1)

if __name__ == "__main__":
        try:
                if len(listOfKeypairs) == int(0):
                        print("\nYou do not have any UTXOs yet")
                        print("\nMake a new UTXO and fund it before consolidating your UTXO")
                        exit(0)

                else:
                        prompt_send_algos()

        except:
                revert_moved_utxo()
