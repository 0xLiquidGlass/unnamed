from ..globals.FilePaths import keyfilePath
from ..globals.Encoding import encoding
from os import urandom
from base64 import b64encode

def make_keyfile():
	print("Please insert and mount your external drive to add the keyfile in")
	print("\n\nNote: The external drive path must be the same as the path specified in the setup process")
	input("\n\nOnce You are done, press enter to continue")
	with open (keyfilePath, "w") as writeToKeyfile:
		binaryUrandomData = urandom(64)
		stringUrandomData = binaryUrandomData.decode(encoding)
		writeToKeyfile.write(stringUrandomData)
	print("\n\nPlease keep your keyfile offline when not in use")
	print("\n\nAnyone who has your keyfile can weaken your wallet's security")

if __name__ == "__main__":
	make_keyfile()
