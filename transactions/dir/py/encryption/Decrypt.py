# In case
from ..wipe.ShredFile import

from CheckForKeyfile import check_for_keyfile
from nacl import secret, utils, pwhash
from getpass import getpass

def decrypt_ciphertext(ciphertextData):
	decryptedData = box.decrypt(ciphertextData)
        box = secret.SecretBox(key)
	return decryptedData

def compare_password(storedHash):
	currentHash = pwhash.str(obtain_decryption_key())
	result = pwhash.verify(currentHash, storedHash)
	return result

def obtain_decryption_key():
        password = getpass(prompt = "\n\nPassword: ")
        input("\n\nInsert your external drive containing the keyfile and mount it\n\nPress enter to continue")
        key = password + check_for_keyfile()
	return key
