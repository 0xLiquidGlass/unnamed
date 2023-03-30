"""
Written by Liquid Glass

Useable functions when imported:

1. decrypt_ciphertext(ciphertextData, stretchedKey)

Where ciphertextData is the ciphertext and stretchedKey
is the key that is used to encrypt the plaintext
"""

from globals.Encoding import textEncodingFormat
from nacl import secret, utils, pwhash

def decrypt_ciphertext(ciphertextData, stretchedKey):
        box = secret.SecretBox(stretchedKey)
        byteCiphertextData = ciphertextData
        # For testing
        # print(byteCiphertextData)
        byteDecryptedData = box.decrypt(byteCiphertextData)
        stringDecryptedData = byteDecryptedData.decode(textEncodingFormat)
        return stringDecryptedData
