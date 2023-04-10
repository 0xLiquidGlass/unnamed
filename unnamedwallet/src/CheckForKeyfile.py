"""
Written by Liquid Glass

Useable functions when imported:

1. check_for_keyfile()

The function checks if a filepath exists, and then returns the keyfile data. If
the filepath does not exist, the user will have to input a filepath manually. If
there is no filepath (i.e. the user does not have a keyfile), an empty string
will be passed
"""

from globals.Encoding import textEncodingFormat
from base64 import b64decode
from os import path

def check_for_keyfile():
        try:
                currentKeyfilePath = read_bookmarked_keyfile_path()
                if path.exists(currentKeyfilePath) == True:
                        return read_keyfile_data(currentKeyfilePath)
                else:
                        currentKeyfilePath = manual_input_keyfile_path()
                        return read_keyfile_data(currentKeyfilePath)
        except FileNotFoundError:
                currentKeyfilePath = manual_input_keyfile_path()
                return read_keyfile_data(currentKeyfilePath)

def read_bookmarked_keyfile_path():
        with open("PreviousKeyfilePath.txt", "r") as bookmarkedKeyfilePath:
                bookmarkedKeyfilePath = bookmarkedKeyfilePath.read()
                bookmarkedKeyfilePathNoQuotes = bookmarkedKeyfilePath.strip('"')
        return bookmarkedKeyfilePathNoQuotes

def manual_input_keyfile_path():
        print("\n\nPlease INSERT and MOUNT your external drive for your keyfile")
        print("\n\nIf you do not have a keyfile, press enter")
        inputKeyfilePath = str(input("\n\nKeyfile path: "))
        inputKeyfilePathNoQuotes = inputKeyfilePath.strip('"')
        return inputKeyfilePathNoQuotes

def read_keyfile_data(anyKeyfilePath):
        try:
                if path.exists(anyKeyfilePath) == False:
                        return pass_empty_byte()
                else:
                        with open(anyKeyfilePath, "r") as keyfileData:
                                readKeyfileAscii = keyfileData.read(128)
                                keyfileBytes = b64decode(readKeyfileAscii)
                                return keyfileBytes
        except TypeError:
                return pass_empty_byte()

def pass_empty_byte():
         print("\n\nNo keyfile detected. Will pass as an empty string instead")
         emptyString = ""
         emptyByte = emptyString.encode(textEncodingFormat)
         return emptyByte

if __name__ == "__main__":
        print(check_for_keyfile())
