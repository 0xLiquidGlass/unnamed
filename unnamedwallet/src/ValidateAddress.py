"""
Written by Liquid Glass

Useable functions when imported:

1. validate_address(address)

Where the address can be any address as long as it is a valid address
otherwise, the user will be greeted with "This is not a valid address"
message
"""

from algosdk import encoding

def validate_address(address):
        try:
                if address != "":
                        decodeAddress = encoding.decode_address(address)
                else:
                        return int(1)
        except:
                return int(1)

if __name__ == "__main__":
        while True:
                try:
                        receivingAddress = str(input("\n\nAddress to check: "))
                        returnedCode = validate_address(receivingAddress)
                        if returnedCode == int(0):
                                print("\n\nThis is a valid address")
                        elif returnedCode == int(1):
                                print ("\n\nThis is not a vaid address")
                except KeyboardInterrupt:
                        print("\n\nExiting\n\n")
                        exit(0)
