#!/bin/sh

# Algorand Python SDK
pip install py-algorand-sdk

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
# Docker - To remove the need for sudo
# Might pose a security risk. Remove comment tag when needed
# sudo groupadd docker
# sudo usermod -aG docker $USER
# newgrp docker
clear
read -p "Running Hello World for Docker. Press enter to continue" nil
clear
# Without sudo
docker run hello-world
# With sudo
# sudo docker run hello-world
# Start Docker on boot with systemd
# Comment on the next 2 lines if you do not want to boot with systemd
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

# Golang
# apt repo may not be reliable to get latest version 
# Obtain package directly from golang's site
wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile && source ~/.profile
# Has golang be installed correctly?
read -p "Press enter to see go version. Reinstall if there is an error." nil
go version
