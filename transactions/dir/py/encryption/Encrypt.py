# In case
from ..wipe.ShredFile import

from ..GenerateWallet import generate_keypair
from CheckForKeyfile import check_for_keyfile
from nacl import secret, utils, pwhash
from getpass import getpass

def encrypt_plaintext(plaintextData):
	box = secret.SecretBox(key)
        encryptedData = box.encrypt(plaintextData)
        return encryptedData

def get_password_hash():
	passwordHash = pwhash.str(key)
	return passwordHash

def obtain_encryption_key():
        password = getpass(prompt = "\n\nPassword: ")
        input("\n\nInsert your external drive containing the keyfile and mount it\n\nPress enter to continue")
        key = password + check_for_keyfile()
	return key
