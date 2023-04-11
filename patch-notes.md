# Patch Notes For Unnamed Wallet

## Unnamed Wallet v1.1.0

1. Added ASA functionality

## Unnamed Wallet v1.0.0

1. Modified files for Unnamed Wallet to work properly on Windows

2. When the wallet encounters an error when sending a specified amount, if the change address has a zero balance, the change address will be deleted. Will not delete the change address with positive balance balance (e.g. due to power outage, KeyboardInterrupt, etc)

3. Before sending Algos either by consolidating UTXO balances or sending to someone, if the UTXO's private key cannot be decrypted (e.g. different key is used), the UTXO will be skipped, will continue until all of the UTXOs whose private keys can be decrypted, are prepared for signing. A message will be shown as to which UTXO cannot be decrypted if the UTXO is skipped

4. Added new function if the user wants to use a password duiring encryption

5. Added new function that confirms that the password entered is correct and sufficiently long (at least 12 characters)

6. Before generating a new wallet, the user will have to confirm the password by entering the same password twice

7. Users will now know how many batched transactions are left when sending. Useful for transactions that involve more than 16 UTXOs

8. Users will now be able to import their seed phrase from other wallets and send the remaining balance to Unnamed Wallet with a new address that they own

## Unnamed Wallet v0.0.0 Testing Release

1. Completed Unnamed Wallet for Linux