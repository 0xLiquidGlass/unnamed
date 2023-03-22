from globals.Encoding import encoding
from nacl import secret, utils, pwhash

def encrypt_plaintext(plaintextData, stretchedKey):
        box = secret.SecretBox(stretchedKey)
        nonce = utils.random(secret.SecretBox.NONCE_SIZE)
        byteEncryptedData = box.encrypt(plaintextData, nonce)
        stringEncryptedData = str(byteEncryptedData)
        return stringEncryptedData
