# Unnamed - An Algorand Wallet That Mimics UTXO

### Introduction

This project is an Algorand wallet that is designed to use a new address for every new transaction. It solves the problem related to privacy due to reusing addresses. This wallet will also be able to reduce the chance that your Algos will be stolen from just one account. Think of Unnamed like Algorand's Electrum.

Note that this project is currently work in progress. Many features are not yet developed.

### Motivation

Due to incidences like [signing wallets on malicious websites](https://blockworks.co/news/metamask-moves-to-help-crypto-scam-victims-recover-stolen-digital-assets) or [stolen seed phrase](https://cointelegraph.com/news/stepn-impersonators-stealing-users-seed-phrases-warn-security-experts), it is clear that users must not rely on just one wallet to store all the crypto. This is not easy to do on Algorand as Algorand uses an account model which means that it reuses addresses unlike Bitcoin and Cardano that uses the UTXO model. Therefore, Unnamed solves the issue of compromised wallets by avoiding address reuse and generating a new keypair that is not tied to a master key.

Speaking of address reuse, transaction privacy is also an issue. take a look at this [article](https://en.bitcoin.it/wiki/Address_reuse) on bitcoin.it. I am pretty sure that you do not want all of your savings to be revealed do you? On public ledgers like Algorand, people are able to view the blockchain to confirm that the transactions went through, which is a good thing. This becomes a pain point when users reuse address due to convinience. Unnamed solves the issue of transaction privacy due to address reuse by allowing users of the wallet to generate a new wallet for every transaction and giving users the choice to isolate a keypair for actions that require address reuse.

### What Is It Built On?

[Algorand Python SDK](https://github.com/algorand/py-algorand-sdk)

### Code Architecture

- One file, one purpose in text format

  - For easy portability to other Operating Systems when needed

  - For new features to be added or removed easily

- Self documenting code

  - Easy readability even if someone has no coding knowledge

### Operating System

Linux

### Project Development Related

This project needs someone who can:

1. Do Python
2. Do a proper documentation

If you are interested, please contact me through [Gmail or Twitter](https://github.com/0xLiquidGlass/0xLiquidGlass/blob/main/README.md#contact)

### Donations

If you support this project, please feel free to donate. The proceeds will be used for the development of this project.

``` 
  Algorand: 7VMA5N3QN6EN4DZ5WE4FZB4YTYDLPVELJNPX3GANZ7DMR4DL7YVXKO7WCM
```
