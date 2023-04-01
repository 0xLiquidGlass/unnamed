"""
Written by Liquid Glass

Useable functuions when imported:

1. check_valid_utxo(utxoToCheck)

This function checks the balance for an address (or UTXO for Unnamed Wallet)

If there is a balance of 0, the UtxoZeroBalance exception will be
raised and if there is a balance of less than the dust limit, which
is 3000 micro Algos, the UtxoUnsafeDust exception will be rised
"""

from globals.AlgodUtils import algodClient

class UtxoZeroBalance(Exception):
        pass

class UtxoUnsafeDust(Exception):
        pass

minDustLimit = int(1000)

def check_valid_utxo(utxoToCheck):
        accountInfo = algodClient.account_info(utxoToCheck)
        utxoBalance = accountInfo.get("amount")

        try:
                check_utxo_positive_balance(utxoToCheck, utxoBalance)
                check_utxo_no_dust(utxoToCheck, utxoBalance)
                print("\n{} is good to go" .format(utxoToCheck))

        except UtxoZeroBalance:
                print("\n{} has no balance. This UTXO will not be used" .format(utxoToCheck))

        except UtxoUnsafeDust:
                print("\n{} contains dust that may be harmful to privacy" .format(utxoToCheck))
                print("Moving {} to the unsafe/ directory" .format(utxoToCheck))

def check_utxo_positive_balance(utxoToCheck, utxoBalance):
        if utxoBalance > int(0):
                print("\n{} has positive balance" .format(utxoToCheck))

        else:
                raise UtxoZeroBalance

def check_utxo_no_dust(utxoToCheck, utxoBalance):
        if utxoBalance <= minDustLimit:
                raise UtxoUnsafeDust

        else:
                print("\n{} has no dust. Good to use" .format(utxoToCheck))
