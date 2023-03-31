"""
Written by Liquid Glass

Useable functions when imported:

1. get_key()

Where a password an optional keyfile stored in an external drive is concatenated 
and then encoded to give a final key. To be used with stretch_key(encodedKey, salt)
as the encodedKey parameter

2. generate_kdf_salt()

Where a new salt is generated each time it is called. To be used with
stretch_key(encodedKey, salt) as the salt parameter

3. stretch_key(encodedKey, salt)

Stretches key to give a final key that is longer than the original
The salt parameter can be either newly generated or obtained from an
existing keypair
"""

from globals.Encoding import textEncodingFormat
from CheckForKeyfile import check_for_keyfile
from nacl import secret, utils, pwhash
from getpass import getpass

def get_key():
        textPassword = getpass(prompt = "\n\nPassword: ")
        encodedPassword = textPassword.encode(textEncodingFormat)
        input("\n\nInsert your external drive containing the keyfile and mount it\n\nPress enter to continue")
        encodedKey = encodedPassword + check_for_keyfile()
        return encodedKey

def generate_kdf_salt():
        rawGeneratedSalt = utils.random(pwhash.argon2i.SALTBYTES)
        return rawGeneratedSalt

def stretch_key(encodedKey, salt):
        kdf = pwhash.argon2i.kdf
        operations = pwhash.argon2i.OPSLIMIT_SENSITIVE
        memory = pwhash.argon2i.MEMLIMIT_SENSITIVE
        kdfDerivedKey = kdf(secret.SecretBox.KEY_SIZE, encodedKey, salt, opslimit = operations, memlimit = memory)
        return kdfDerivedKey

if __name__ == "__main__":
        obtainedKey = get_key()
        generatedSalt = initialize_kdf_salt()
        print(strech_key(obtainedKey, generatedSalt))