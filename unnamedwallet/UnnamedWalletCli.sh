#!/bin/sh

# For Debian

sudo ./src/dependencies/sandbox/sandbox up testnet -v -s

clear

echo "Welcome To Unnamed Wallet"
echo

simple_mode () {
	while true
	do
		echo
		echo "1 --> Setup"
		echo
		echo "2 --> Make a keyfile"
		echo
		echo "3 --> Generate a new wallet"
		echo
		echo "4 --> Check Algo balance"
		echo
		echo "5 --> Consolidate UTXOs"
		echo
		echo "6 --> Send Algos to others"
		echo
		echo "7 --> More options"
		echo
		echo "8 --> Quit"
		echo

		echo
		read -p "Your choice: " choice

		if [ "$choice" = "1" ]; then
			clear
			read -p "Installing dependencies. Press enter to continue"
			cd ./src/dependencies/
			source DebianPackages.sh
			read -p "Setup done. Press enter to continue" nil
			cd ../../
			clear

		elif [ "$choice" = "2" ]; then
			clear
			cd ./src/MakeKeyfile.py
			echo
			read -p "Press enter to continue" nil
			cd ../
			clear

		elif [ "$choice" = "3" ]; then
			clear
			cd ./src/
			python3 GenerateWallet.py
			read -p "Press enter to continue"
			cd ../
			clear

		elif [ "$choice" = "4" ]; then
			clear
			cd ./src/
			python3 AssetBalance.py
			read -p "Press enter to go back" nil
			cd ../
			clear

		elif [ "$choice" = "5" ]; then
			clear
			cd ./src/
			python3 ConsolidateWalletBalance.py
			cd ../
			clear

		elif [ "$choice" = "6" ]; then
			clear
			cd ./src
			python3 SendAlgo.py
			cd ../

		elif [ "$choice" = "7" ]; then
			clear
			more_options
			clear

		elif [ "$choice" = "8" ]; then
			clear
			sudo ./src/dependencies/sandbox/sandbox down
			clear
			exit 0

		else
			clear
			echo "Please try again"
			echo
		fi
	done
}

more_options () {
	echo "More options"
	echo
	while true
	do
		echo
		echo "1 --> Check if an address is valid"
		echo
		echo "2 --> Show previously generated unused address"
		echo
		echo "3 --> To go back"
		echo

		echo
		read -p "Your choice: " moreChoice

		if [ "$moreChoice" = "1" ]; then
			clear
			cd ./src/
			python3 ValidateAddress.py
			cd ../
			clear

		elif [ "$moreChoice" = "2" ]; then
			clear
			cd ./src/
			python3 ListUnusedUtxos.py
			clear

		elif [ "$moreChoice" = "3" ]; then
			clear
			break

		else
			clear
			echo "Please try again"
			echo
		fi
	done
}

simple_mode
