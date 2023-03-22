from globals.FilePaths import keyfilePath
from os import path

def check_for_keyfile():

        if path.exists(keyfilePath) == False:
                return ""
        else:
                with open(keyfilePath, "r") as keyfileData:
                        keyfileData.read(128)
                        return keyfileData

