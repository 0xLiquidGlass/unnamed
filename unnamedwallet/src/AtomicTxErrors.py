"""
Written by Liquid Glass

Useable functuions when imported:

1. check_valid_utxo(utxoToCheck)

This function checks the balance for an UTXO (or account for general use)

If there is a balance of 0, the UtxoZeroBalance exception will be
raised and if there is a balance of less than the dust limit, which
is 3000 micro Algos, the UtxoUnsafeDust exception will be rised

These are the error codes for each possibilities depending on
the balance of each UTXO:

0 --> No zero balance, no dust

1 --> Zero balance

2 --> Has dust, no zero balance
"""

from globals.AlgodUtils import algodClient
from globals.ValueConstants import txFeeConst, keepAccountAliveAmountConst

class UtxoZeroBalance(Exception):
        pass

class UtxoUnsafeDust(Exception):
        pass

minDustLimit = (keepAccountAliveAmountConst * 3)

def check_valid_utxo(utxoToCheck):
        accountInfo = algodClient.account_info(utxoToCheck)
        utxoBalance = accountInfo.get("amount")

        try:
                check_utxo_positive_balance(utxoToCheck, utxoBalance)
                check_utxo_no_dust(utxoToCheck, utxoBalance)
                print("\n{} is good to go" .format(utxoToCheck))
                return int(0)

        except UtxoZeroBalance:
                print("\n{} has no balance. This UTXO will not be used" .format(utxoToCheck))
                return int(1)

        except UtxoUnsafeDust:
                print("\n{} contains dust that may be harmful to privacy" .format(utxoToCheck))
                print("\nMoving {} to the unsafe/ directory" .format(utxoToCheck))
                return int(2)

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
