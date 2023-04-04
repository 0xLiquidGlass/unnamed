"""
Written by Liquid Glass
"""

from algosdk.v2client import algod

algodAddress = "https://testnet-algorand.api.purestake.io/ps2"
algodToken = "4Pn3HIVDrL6iCNtnvPP76aPqOEKU4L1Z1lZv3ZhE"

headers = {
   "X-API-Key": algodToken,
}

algodClient = algod.AlgodClient(algodToken, algodAddress, headers)
