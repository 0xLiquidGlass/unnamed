#!/bin/sh

mkdir ./dir/wallet
mkdir ./dir/wallet/transaction
mkdir ./dir/wallet/transaction/unspent
mkdir ./dir/wallet/transaction/spent

# Algorand Python SDK
pip install py-algorand-sdk

# Golang
# apt repo may not be reliable to get latest version
# Obtain package directly from golang's site instead
wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile && source ~/.profile
read -p "Press enter to see go version. Reinstall if there is an error." nil
clear
go version
read -p "Press enter to continue" nil

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
clear
read -p "Running Hello World for Docker. Press enter to continue" nil
clear
sudo docker run hello-world

# Install Algorand's sandbox
git clone https://github.com/algorand/sandbox.git
cd sandbox
sudo ./sandbox up mainnet -v -s
cd ../
