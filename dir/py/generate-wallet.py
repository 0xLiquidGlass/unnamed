#!/bin/py

from algosdk import account, mnemonic

def generate_keypair ():
	private_key, address = account.generate_account()
	new_document_path.write("Address: {}\n\n" .format(address))
	new_document_path.write("Seed: {}" .format(mnemonic.from_private_key(private_key)))

filename = input("Name of File: ")

new_document_path = open("../wallets/"+filename+".txt", "x")

generate_keypair()

new_document_path.close()

print("Please Keep The Newly Generated Keypair Safe!\n\nAnyone Who Has Your Seed CAN Spend Your Algos!")
