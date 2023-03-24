from globals.Encoding import encoding
from CheckForKeyfile import check_for_keyfile
from nacl import secret, utils, pwhash
from getpass import getpass

def get_key():
        password = getpass(prompt = "\n\nPassword: ")
        input("\n\nInsert your external drive containing the keyfile and mount it\n\nPress enter to continue")
        key = password + check_for_keyfile()
        encodedKey = key.encode(encoding)
        kdf = pwhash.argon2i.kdf
        salt = utils.random(pwhash.argon2i.SALTBYTES)
        operations = pwhash.argon2i.OPSLIMIT_SENSITIVE
        memory = pwhash.argon2i.MEMLIMIT_SENSITIVE
        kdfDerivedKey = kdf(secret.SecretBox.KEY_SIZE, encodedKey, salt, opslimit = operations, memlimit = memory)
        return kdfDerivedKey

if __name__ == "__main__":
	print (get_key())
