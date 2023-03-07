from algosdk.v2client import algod

algodAddress = "http://localhost:4001"
algodToken = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algodClient = algod.AlgodClient(algodToken, algodAddress)