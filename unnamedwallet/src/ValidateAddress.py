"""
Written by Liquid Glass

Useable functions when imported:

1. validate_address(address)

Where the address can be any address as long as it is a valid address
otherwise, the user will be greeted with "This is not a valid address"
message
"""

from algosdk import encoding

class NotValidAddress(Exception):
        pass

def validate_address(address):
        try:
                if address != "":
                        decodeAddress = encoding.decode_address(address)
                else:
                        raise NotValidAddress
        except:
                raise NotValidAddress

if __name__ == "__main__":
        while True:
                try:
                        receivingAddress = str(input("\n\nAddress to check: "))
                        validate_address(receivingAddress)
                        print("\n\nThis is a valid address")
                        break
                except NotValidAddress:
                        print ("\n\nThis is not a vaid address")
                except KeyboardInterrupt:
                        print("\n\nExiting\n\n")
                        exit(0)
