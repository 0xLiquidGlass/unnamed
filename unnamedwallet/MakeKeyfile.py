"""
Written by Liquid Glass
"""

from globals.FilePaths import keyfilePath
from globals.Encoding import textEncodingFormat
from os import urandom, path.exists

def make_keyfile():
	print("\n\nPlease insert and mount your external drive for your keyfile")
        print("\n\nOnce you are done, enter the full file path to the external drive below")
	inputKeyfilePath = str(input("\nKeyfile path: "))
        write_keyfile_data(inputKeyfilePath)
        check_path_written()
        write_keyfile_data(keyfilePath)

def write_keyfile_path(inputKeyfilePath):
        with open("../globals/Filepaths.py", "a+") as checkKeyfilePath:
                readFilePaths = checkKeyfilePath.readlines()
                keywordFound = False
                for line in readFilePaths:
                        if "keyfilePath" in line:
                                keywordFound = True
                                break
                if keywordFound == False:
                        checkKeyfilePath.write("KeyfilePath = {}/UnnamedKeyfile.txt" .format(keyfilePath))

def write_keyfile_data(keyfilePath):
        with open (keyfilePath, "w") as writeToKeyfile:
                binaryUrandomData = urandom(64)
                stringUrandomData = binaryUrandomData.decode(textEncodingFormat)
                writeToKeyfile.write(stringUrandomData)
                print("\n\nPlease keep your keyfile offline when not in use")
                print("\n\nAnyone who has your keyfile can weaken your wallet's security")

def check_path_written():
        if path.exists(keyfilePath):
                print("\n\nYou have successfully made a keyfile")
        else:
                print("\n\nSomething is wrong. Please make the keyfile again")
                make_keyfile()

if __name__ == "__main__":
	make_keyfile()
