#!/bin/sh

# For Fedora, RedHat and distros derived from Fedora and RedHat

# Install wallet directories
mkdir ../wallet
mkdir ../wallet/transaction
mkdir ../wallet/transaction/unspent
mkdir ../wallet/transaction/spent
mkdir ../wallet/transaction/unsafe


# Install Python packages

if command -v dnf >/dev/null 2>&1; then
  # Fedora or Red Hat 8 or later
    sudo dnf install python3-pip
    sudo dnf install python3-tkinter
else
    # Red Hat 7 or earlier
    sudo yum install python3-pip
    sudo yum install python3-tkinter
fi

pip install pynacl
pip install py-algorand-sdk
