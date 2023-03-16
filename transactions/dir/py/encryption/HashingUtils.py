from nacl import pwhash

def get_password_hash(stretchedKey):
        passwordHash = pwhash.str(stretched_key())
        return passwordHash

def compare_password(storedHash):
        currentHash = pwhash.str(stretched_key())
        result = pwhash.verify(currentHash, storedHash)
        return result
