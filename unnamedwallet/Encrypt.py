from globals.Encoding import encoding
from nacl import secret, utils, pwhash

def encrypt_plaintext(stringPlaintextData, stretchedKey):
        box = secret.SecretBox(stretchedKey)
        nonce = utils.random(secret.SecretBox.NONCE_SIZE)
        bytePlaintextData = stringPlaintextData.encode(encoding)
        byteEncryptedData = box.encrypt(bytePlaintextData, nonce)
        # For testing
        # print(byteEncryptedData)
        return byteEncryptedData
