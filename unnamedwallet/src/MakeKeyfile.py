"""
Written by Liquid Glass

Useable functions when imported:

1. make_keyfile()

Where this function will first detect from a cache if the keyfile is exist (provided that the
external drive is mounted properly). Otherwise, the user will be prompted to manually input the
path to the keyfile

If the file (not just keyfiles) is detected, the user will be asked whether to overwrite the file
to be used as a keyfile. Will exit if the user says no but will carry on with overwriting the file
if yes
"""

from globals.Encoding import textEncodingFormat
from os import path, urandom
from base64 import b64encode

def make_keyfile():
        try:
                with open("PreviousKeyfilePath.txt", "r") as previousKeyfilePath:
                        currentKeyfilePath = previousKeyfilePath.read()
                with open(currentKeyfilePath, "r") as testOpenBookmarkedKeyfilePath:
                        ask_if_overwrite_existing_file(currentKeyfilePath)
        except FileNotFoundError:
                manual_input_keyfile_path()
        except IOError:
                print("\n\nThis path could not be accessed")
                exit(1)

def manual_input_keyfile_path():
        print("\n\nEnsure that you have INSERTED and MOUNTED your external drive for your keyfile properly")
        print("\n\nEnter the full path to the external drive below")
        inputKeyfilePath = str(input("\n\nKeyfile path: "))
        inputKeyfilePathNoQuotes = inputKeyfilePath.strip('"')
        if path.exists(inputKeyfilePathNoQuotes) == True:
                bookmark_keyfile_path(inputKeyfilePathNoQuotes)
                ask_if_overwrite_existing_file(inputKeyfilePathNoQuotes)
        else:
                bookmark_keyfile_path(inputKeyfilePathNoQuotes)
                generate_keyfile_urandom_data(inputKeyfilePathNoQuotes)

def ask_if_overwrite_existing_file(anyKeyfilePath):
        existingFileOverwrite = str(input("\n\nThis file exists. Overwrite? (y/n): "))
        if existingFileOverwrite == ("y" or "Y"):
                generate_keyfile_urandom_data(anyKeyfilePath)
        elif existingFileOverwrite == ("n" or "N"):
                exit(0)
        else:
                print("\n\nNot sure about that choice. Try again")
                ask_if_overwrite_existing_file(anyKeyfilePath)

def bookmark_keyfile_path(inputKeyfilePath):
        with open("PreviousKeyfilePath.txt", "w") as bookmarkKeyfilePath:
                bookmarkKeyfilePath.write(inputKeyfilePath)

def generate_keyfile_urandom_data(anyKeyfilePath):
        try:
                with open(anyKeyfilePath, "w") as createNewKeyfile:
                        urandomBytes = urandom(64)
                        urandomAscii = b64encode(urandomBytes)
                        urandomString = urandomAscii.decode(textEncodingFormat)
                        createNewKeyfile.write(urandomString)
                print("\n\nThe file has been written with keyfile data")
        except FileNotFoundError:
                print("\n\nThe path could not be found. Please try again")
                manual_input_keyfile_path()
        except PermissionError:
                print("\n\nThis file does not support write operations")
                print("\n\nChoose another one")
                manual_input_keyfile_path()
                

if __name__ == "__main__":
        make_keyfile()
