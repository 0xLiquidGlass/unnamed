#!/bin/bash

<<comment
To do:
1. Add more choices, with documentation placed at the end when all of Python programs are done
2. Implement "sandbox down" and "exit" when all of Python programs are done
comment

# For Debian

dir/sh/dependencies/sandbox/sandbox up mainnet -v -s

clear

while true
do
	echo -e "This is an Algorand wallet that is designed for merchants and normal users alike.\n\n1 --> Setup\n\n2 --> Generate a new wallet\n\n3 --> Documentation\n"

	read -p "Your choice: " choice

	# 1 for setup (install dependencies needed to run app)
	# 2 for generating new wallet
	# 3 for documentation
	# More features will be added
	
        if [ $choice == 1 ]; then
                clear
                echo "Installing required dependencies"
                sh ./dir/sh/dependencies/debian-packages.sh
                read -p "Done. Press enter to continue"

        elif [ $choice == 2 ]; then
                clear
		cd ./dir/wallets/ 
		python3 ../py/GenerateWallet.py
		cd ../..

        elif [ $choice == 3 ]; then
                clear
                xdg-open ./dir/readme/README.pdf
        fi
done
