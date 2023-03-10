#!/bin/sh

mkdir ./dir/wallet
mkdir ./dir/wallet/transaction
mkdir ./dir/wallet/transaction/unspent
mkdir ./dir/wallet/transaction/spent

# Algorand Python SDK
pip install py-algorand-sdk