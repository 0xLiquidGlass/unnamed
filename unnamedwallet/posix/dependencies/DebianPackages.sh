#!/bin/sh

# For Debian and distros derived from Debian like:
# Ubuntu and Tails OS

# Install wallet directories
mkdir ../wallet
mkdir ../wallet/transaction
mkdir ../wallet/transaction/unspent
mkdir ../wallet/transaction/spent
mkdir ../wallet/transaction/unsafe


# Install Python packages
sudo apt install python3-pip
sudo apt install python3-tk
pip install py-algorand-sdk
pip install pynacl
