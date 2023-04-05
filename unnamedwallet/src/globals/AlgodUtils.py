"""
Written by Liquid Glass
"""

from algosdk.v2client import algod

algodAddress = "https://testnet-algorand.api.purestake.io/ps2"
algodToken = ""

headers = {
   "X-API-Key": algodToken,
}

algodClient = algod.AlgodClient(algodToken, algodAddress, headers)
