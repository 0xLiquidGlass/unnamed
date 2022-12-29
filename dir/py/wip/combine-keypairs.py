def query_all_wallets():

	wallet_path = "../wallets/"

	counter = 0

	for number_of_files in os.listdir(wallet_path):

		if os.path.isfile(os.path.join(wallet_path, path)):

			counter += 1

	# Testing for next 2 lines

	print ("Number of Files: ", counter)

query_all_wallets()
