from ..FilePaths import keyfilePath
from ..wipe.ShredFile import
from pynacl import secret, utils
from getpass import getpass

def encrypt_plaintext(plaintextData):
        password = getpass(prompt = "\n\nPassword: ")
        key = password + check_for_keyfile()
	box = secret.SecretBox(key)
        encryptedData = box.encrypt(plaintextData)
        return encryptedData

def check_for_keyfile():
	if keyfilePath == "":
		return ""
	else:
		with open(keyfilePath, "r") as keyfileData:
			keyfileData.read(128)
			return keyfileData

if __name__ == "__main__":
	print(encrypt_plaintext("Some message"))
