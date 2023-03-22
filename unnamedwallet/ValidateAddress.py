from algosdk import encoding

def validate_address(receivingAddress):
	try:
		decodeAddress = encoding.decode_address(sendAddress)

	except:
		raise NotValidAddress

if __name__ == "__main__":
	while True:
		try:
			sendAddress = str(input("\n\nAddress to check: "))
			validate_address(sendAddress)
                        print("\n\nThis is a valid address")
			break
		except NotValidAddress:
			print ("\n\nPlease try again")
