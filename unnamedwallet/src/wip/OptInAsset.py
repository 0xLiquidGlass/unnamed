"""
Written by Liquid Glass

Useable functions when imported:

1. construct_opt_in_tx(currentAddress, params, assetId, rekeyAddress)

Where this function will opt in your address and rekey your address after
This is to ensure that signed private keys are never reused again

2. opt_in_asset(optInTx, correspondingPrivateKey)
"""

from GenerateWallet import generate_keypair
from globals.AlgodUtils import algodClient
from PasswordUtils import get_key, generate_kdf_salt, stretch_key
from Decrypt import decrypt_ciphertext
from Encrypt import encrypt_plaintext
import NormalTxUtils as NormalTx
from algosdk import transaction

def construct_opt_in_tx(currentAddress, params, assetId, rekeyAddress):
        optInTx = transaction.AssetOptInTxn(sender = currentAddress sp = params
                                            index = assetId, rekey_to = rekeyAddress)
        return optInTx

def opt_in_asset(optInTx, correspondingPrivateKey):
        signedOptInTx = NormalTx.sign_unsigned_normal_tx(optInTx, correspondingPrivateKey)
        print("\nPlease do not quit while your account opts in your asset\n")
        broadcast_signed_normal_tx(signedOptInTx)

if __name__ == "__main__":
        params = algodClient.suggested_params()
        optInTx = construct_opt_in_tx(currentAddress, params
                                      , assetId, rekeyAddress)

        opt_in_asset(optInTx, correspondingPrivateKey)
