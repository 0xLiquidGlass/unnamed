#!/bin/bash

<<comment
To do:
1. Implement "sandbox down" on exit
comment

# For Debian

dir/sh/dependencies/sandbox/sandbox up mainnet -v -s

clear

echo "Welcome To Unnamed Wallet\n\n"

while true
do
	echo "1 --> Setup\n\n2 --> Generate a new wallet\n\n3 --> Check Algo balance\n\n4 --> Consolidate UTXOs\n\n5 --> Documentation\n"

	read -p "Your choice: " choice

	# 1 for setup (install dependencies needed to run app)
	# 2 for generating new wallet
	# 3 to check balance
	# 4 to consolidate balance
	# 5 to send to others (WIP)
	# 6 for documentation (option 5 for now)
	
        if [ $choice = 1 ]; then
                clear
                echo "Installing required dependencies"
                sh ./dir/sh/dependencies/debian-packages.sh
		clear
                read -p "Done. Press enter to continue"

        elif [ $choice = 2 ]; then
                clear 
		python3 ./dir/py/GenerateWallet.py

        elif [ $choice == 3 ]; then
                clear
                python3 ./dir/py/AssetBalance.py

        elif [ $choice == 4 ]; then
                clear
                python3 ./dir/py/ConsolidateWalletBalance.py

        elif [ $choice == 5 ]; then
                clear
                xdg-open ./dir/readme/README.pdf

	# else
		# clear
		# echo "Please try again\n\n"
        fi
done
