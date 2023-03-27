"""
Written by Liquid Glass

Useable functions when imported:

1. make_keyfile()

This functions asks for a valid filepath from the user. If
the filepath is valid, the program will make a file and writes
random data (using os.urandom) into the file that will become
a keyfile. If the filepath is invalid or the user presses enter,
no keyfile will be made and instead the keyfilePath will be written
as empty. Users can go directly to FilePaths.py in the globals/
directory to change the filepath string
"""

from globals.FilePaths import keyfilePath
from globals.Encoding import textEncodingFormat
from os import urandom, path.exists

def make_keyfile():
	print("\n\nPlease INSERT and MOUNT your external drive for your keyfile")
        print("\n\nOnce you are done, enter the full file path to the external drive below")
        print("\n\nIf you do not want a keyfile, press enter")
	inputKeyfilePath = str(input("\n\nKeyfile path: "))
        check_if_filepath_exists(inputKeyfilePath)

def check_if_filepath_exists(inputKeyfilePath):
        if path.exists(inputKeyfilePath) == True:
                write_keyfile_path(inputKeyfilePath)
                check_path_written()
                write_keyfile_data(keyfilePath)
        else:
                write_empty_keyfile_path()

def write_keyfile_path(inputKeyfilePath):
        with open("globals/FilePaths.py", "a+") as checkKeyfilePath:
                readFilePaths = checkKeyfilePath.readlines()
                keywordFound = False
                for line in readFilePaths:
                        if "keyfilePath" in line:
                                keywordFound = True
                                break
                        if keywordFound == False:
                                checkKeyfilePath.write("keyfilePath = {}/UnnamedKeyfile.txt" .format(keyfilePath))
                                break

def write_empty_keyfile_path():
        with open("globals/FilePaths.py", "a+") as writeEmptyKeyfilePath:
                readFilePaths = writeEmptyKeyfilePath.readlines()
                keywordFound = False
                for line in readFilePaths:
                        if "keyfilePath" in line:
                                keywordFound = True
                                break
                        if keywordFound = False:
                                writeEmptyKeyfilePath.write("keyfilePath = {}".format(""))
                                break

def write_keyfile_data(keyfilePath):
        with open(keyfilePath, "w") as writeToKeyfile:
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
        try:
	        make_keyfile()
        except ImportError:
                make_keyfile()
