@echo on

mkdir ..\wallet
mkdir ..\wallet\transaction
mkdir ..\wallet\transaction\unspent
mkdir ..\wallet\transaction\spent
mkdir ..\wallet\transaction\unsafe

pip install pynacl
pip install py-algorand-sdk
