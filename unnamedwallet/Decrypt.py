from globals.Encoding import encoding
from nacl import secret, utils, pwhash

def decrypt_ciphertext(ciphertextData, stretchedKey):
        box = secret.SecretBox(stretchedKey)
        stringCiphertextData = ciphertextData
        byteCiphertextData = stringCiphertextData.encode(encoding)
        byteDecryptedData = box.decrypt(byteCiphertextData)
        stringDecryptedData = byteDecryptedData.decode(encoding)
        return stringDecryptedData