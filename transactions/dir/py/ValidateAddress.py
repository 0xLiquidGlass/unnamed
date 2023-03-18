from algosdk import encoding

def validate_address(sendAddress):
	try:
		decodeAddress = encoding.decode_address(sendAddress)
		return True

	except:
		return False

if __name__ == "__main__":
	while True:
		try:
			sendAddress = str(input("\n\nAddress to check: "))
			validate_address(sendAddress)
			break
		except:
			print ("\n\nPlease try again")

		except KeyboardInterrupt:
			exit()

	if validate_address() == False:
		print ("Not a valid address")
	else:
		print ("Valid address")
