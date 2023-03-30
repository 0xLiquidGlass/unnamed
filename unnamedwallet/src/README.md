# Why You Should Use Unnamed Wallet?

## 1. Privacy Features

### a. UTXO-like behaviour

- UTXO if implemented and used correctly, can give you good privacy as every [address is used once](https://blog.wasabiwallet.io/risks-associated-with-address-reuse/). Our identity is more likely to be associated to an address the more we use it

### b. Checks for dust UTXOs before spending an UTXO

- [Dusting can potentially compromise your privacy](https://www.gemini.com/cryptopedia/crypto-dusting-attack-bitcoin#section-who-would-perform-a-dusting-attack) through revealing of savings or revealing your identity

- For this reason, Unnamed Wallet separates spent accounts and addresses which has dusts (very small amounts of Algo in the address) from the unspent addresses that has larger amounts of Algo

### c. Unsafe UTXO handling

- Spent addresses are more likely to be dusted as the address has already been exposed to the blockchain

- New, unused addresses are not exposed on the blockchain as no transactions has taken place yet, and the blockchain has not recorded any transactions related to the address yet

- For this reason, Unnamed Wallet encourages the use of new, unused addresses

### d. Portability

- You can always take your wallet offline if you want and you can generate new addresses offline from a different machine

## 2. Security Features

### a. pynacl

- Unnamed Wallet uses NaCl library to secure the wallet keypairs each time it is generated

### b. Keyfile or Passwords or Both

- Humans are very bad at entropy, which simply means making a random password that is secure and on top of that, we are not very good at remembering long, complex passwords

- Keyfiles gives you the ability to have long, complex passwords without having to remember them. An external drive like a USB drive or a hard disk can get you started

- Keyfiles is used in apps like [Keepass](https://keepass.info/help/base/keys.html#keyfiles) and [Veracrypt](https://veracrypt.eu/en/Keyfiles.html)

- By using passwords and keyfile, you can be assured that your wallet is safe from [brute force attacks](https://en.wikipedia.org/wiki/Brute-force_attack) as keyfiles can act as a two factor authentication tool

- In Unnamed Wallet, you can use either keyfiles, passwords or both. Your choice

### c. Don't trust, verify

- Unnamed Wallet's source code is open sourced, which means you can study, modify and redistribute the code

- Unnamed Wallet's source code is supposed to be used as is, which means you can always verify if the wallet you are using is malicious just by verifying the code with a text editor

### d. Less exposure of encryption keys when viewing balances

- By default, Unnamed Wallet does not need passwords or keyfiles to view balances in order to reduce the unnecessary exposure of encryption keys

- Encryption keys are only needed when decrypting private keys used for spending

### e. Encourage use of Non-Deterministic keys

- Unnamed Wallet has chosen the Non-Deterministic method of key generation, where every private key is a master key instead of every private key is tied to one master key, which is how all Hierarchical Deterministic wallets work

- Even though Hierarchical Deterministic wallets are easier to backup, Non Deterministic wallets can increase security of the wallet in the event where keys that had been generated a long time ago has been compromised like [this example](https://www.reddit.com/r/ledgerwallet/comments/1239fly/all_my_bitcoin_was_liquidated_from_my_ledger/), no future keys generated will be compromised

- You can read what are Hierarchical Deterministic wallets and how they came about [here](https://www.ledger.com/academy/crypto/what-are-hierarchical-deterministic-hd-wallets) and [here](https://en.bitcoin.it/wiki/Deterministic_wallet) respectively