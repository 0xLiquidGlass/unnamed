"""
Written by Liquid Glass

Useable functions when imported:

1. get_key()

Where a password an optional keyfile stored in an external drive is concatenated 
and then encoded to give a final key. To be used with stretch_key(encodedKey, salt)
as the encodedKey parameter

The use of get_key() is discouraged unless it is used for decryption

2. get_key_for_encryption()

This function is similar to get_key() but it only passes the password when the
password is correct by entering the password twice. Crucial for encryption

3. validate_password()

This function will check if the password is correct by making the user enter the
same password twice. Returns the password if the password is correct but will
restart the process if the password is not correct

4. generate_kdf_salt()

Where a new salt is generated each time it is called. To be used with
stretch_key(encodedKey, salt) as the salt parameter

5. stretch_key(encodedKey, salt)

Stretches key to give a final key that is longer than the original
The salt parameter can be either newly generated or obtained from an
existing keypair
"""

from globals.Encoding import textEncodingFormat
from CheckForKeyfile import check_for_keyfile
from PasswordChecker import check_password_conditions
from nacl import secret, utils, pwhash
from getpass import getpass

def get_key():
        textPassword = getpass(prompt = "\n\nPassword (If no password, press enter): ")
        encodedPassword = textPassword.encode(textEncodingFormat)
        input("\n\nInsert your external drive containing the keyfile and mount it\n\nPress enter to continue")
        encodedKey = encodedPassword + check_for_keyfile()
        return encodedKey

def get_key_for_encryption():
        passwordSwitch = ask_if_use_password()

        if passwordSwitch == int(0):
                textPassword = validate_password()
                encodedPassword = textPassword.encode(textEncodingFormat)
        elif passwordSwitch == int(1):
                print("\n\nUsing a keyfile instead")
                emptyString = str("")
                encodedPassword = emptyString.encode(textEncodingFormat)

        input("\n\nInsert your external drive containing the keyfile and mount it\n\nPress enter to continue")
        encodedKey = encodedPassword + check_for_keyfile()
        return encodedKey

def validate_password():
        while True:
                firstAttempt = getpass(prompt = "\n\nPassword: ")
                secondAttempt = getpass(prompt = "\nConfirm Password: ")
                checkedPasswordStatus = check_password_conditions(firstAttempt, secondAttempt)
                if checkedPasswordStatus == None:
                        print("\nPlease try again")

                else:
                        return checkedPasswordStatus

def ask_if_use_password():
        while True:
                usePasswordChoice = str(input("\n\nDo you want to use a password? (y/n): "))
                if usePasswordChoice == ("y" or "Y"):
                        return int(0)
                elif usePasswordChoice == ("n" or "N"):
                        return int(1)
                else:
                        print("\nPlease try again")

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
