"""
Written by Liquid Glass

Useable functions when imported:

1. encrypt_plaintext(stringPlaintextData, stretchedKey)

Where stringPlaintextData is the plaintext and stretchedKey
is the key that is used to encrypt the plaintext
"""

from globals.Encoding import textEncodingFormat
from nacl import secret, utils, pwhash

def encrypt_plaintext(stringPlaintextData, stretchedKey):
        box = secret.SecretBox(stretchedKey)
        nonce = utils.random(secret.SecretBox.NONCE_SIZE)
        bytePlaintextData = stringPlaintextData.encode(textEncodingFormat)
        byteEncryptedData = box.encrypt(bytePlaintextData, nonce)
        # For testing
        # print(byteEncryptedData)
        return byteEncryptedData
