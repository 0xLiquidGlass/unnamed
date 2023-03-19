from ..globals.encoding import encoding
from nacl import secret, utils, pwhash

def encrypt_plaintext(plaintextData, stretchedKey):
	box = secret.SecretBox(stretched_key())
	nonce = utils.random(secret.SecretBox.NONCE_SIZE)
        encryptedData = box.encrypt(plaintextData, nonce)
        return encryptedData.decode(encoding)
