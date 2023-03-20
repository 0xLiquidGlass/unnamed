#!/bin/sh

function create_wallet_directories() {
	mkdir ../../wallet
	mkdir ../../wallet/transaction
	mkdir ../../wallet/transaction/unspent
	mkdir ../../wallet/transaction/spent
}

function install_python_packages() {
	sudo apt install python3-pip
	pip install py-algorand-sdk
	pip install pynacl
}

function install_golang() {
	# apt repo may not be reliable to get latest version
	# Obtain package directly from golang's site instead
	wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz
	sudo rm -rf /usr/local/go
	sudo tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz
	rm go1.20.1.linux-amd64.tar.gz
	if grep -wq "export PATH=$PATH:/usr/local/go/bin" ~/.profile ; then
		echo
	else
		echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile
	fi
	source ~/.profile
	read -p "Press enter to see go version. Reinstall if there is an error." nil
	go version
	read -p "Press enter to continue" nil
	clear
}

function install_docker() {
	# Docker, according to https://docs.docker.com/engine/install/debian/
	sudo apt-get remove docker docker-engine docker.io containerd runc
	sudo apt-get update
	sudo apt-get install \
	        ca-certificates \
	        curl \
	        gnupg \
                lsb-release
	sudo mkdir -m 0755 -p /etc/apt/keyrings
	curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
        echo \
                "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  		$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt-get update
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
	read -p "Running Hello World for Docker. Press enter to continue" nil
	clear
	sudo docker run hello-world
	read -p "Press enter to continue" nil
}

function install_algorand_sandbox() {
	git clone https://github.com/algorand/sandbox.git
	cd sandbox
	sudo ./sandbox up mainnet -v -s
	cd ../
}

create_wallet_directories
install_python_packages
install_golang
install_docker
install_algorand_sandbox
clear
