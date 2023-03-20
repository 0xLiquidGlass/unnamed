#!/bin/bash

# For Debian

sudo ./dir/sh/dependencies/sandbox/sandbox up mainnet -v -s

clear

echo -e "Welcome To Unnamed Wallet\n\n"

while true
do
	echo -e "1 --> Setup"
	echo -e "\n\n2 --> Generate a new wallet"
	echo -e "\n\n3 --> Check Algo balance"
	echo -e "\n\n4 --> Consolidate UTXOs"
	echo -e "\n\n5 --> Documentation"
	echo -e "\n\n6 --> Quit\n"

	read -p "Your choice: " choice

	# 1 for setup (install dependencies needed to run app)
	# 2 for generating new wallet
	# 3 to check balance
	# 4 to consolidate balance
	# 5 to send to others (WIP)
	# 6 for documentation (option 5 for now)
	# 7 to exit program (option 6 for now)
	# "advanced-mode" for advanced mode

        if [ "$choice" = "1" ]; then
                clear
		read -p "Installing dependencies. Press enter to continue"
		cd ./dir/sh/dependencies/
		source DebianPackages.sh
		read -p "Setup done. Press enter to continue" nil
		cd ../../../
		clear

        elif [ "$choice" = "2" ]; then
                clear
		cd ./dir/py/unnamedwallet/
		python3 GenerateWallet.py
		read -p "Press enter to continue"
		cd ../../../
		clear

        elif [ "$choice" = "3" ]; then
                clear
		cd ./dir/py/unnamedwallet/
                python3 AssetBalance.py
		read -p "Press enter to go back" nil
                cd ../../../
                clear

        elif [ "$choice" = "4" ]; then
                clear
		cd ./dir/py//unnamedwallet/
                python3 ConsolidateWalletBalance.py
		cd ../../../
		clear

        elif [ "$choice" = "5" ]; then
                clear
		cd ./dir/readme/
                xdg-open README.pdf
		cd ../../

        elif [ "$choice" = "6" ]; then
                clear
		sudo ./dir/sh/dependencies/sandbox/sandbox down
		clear
                exit 0

	else
		clear
		echo "Please try again\n\n"
        fi
done
