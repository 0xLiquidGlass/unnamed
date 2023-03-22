from globals.Encoding import encoding
from nacl import secret, utils, pwhash

def decrypt_ciphertext(ciphertextData, stretchedKey):
        box = secret.SecretBox(stretchedKey)
        decryptedData = box.decrypt(ciphertextData)
        return decryptedData.decode(encoding)
