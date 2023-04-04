# Unnamed - An Algorand Wallet That Mimics UTXO

## Introduction

Unnamed wallet is built with mainly privacy, and security in mind. The project was originally thought of as a solution to combat successful attempts on phishing attacks by leveraging Public Key Cryptography, which all cryptocurrency wallet uses.

Unnamed wallet mimics Unspent Transaction Outputs, or UTXO for short. This is the model used by Bitcoin to solve the double spending problem by not reusing the same address twice after the address has been spent. The wallet will use the properties of privacy and security present in UTXO without using the Algorand blockchain to ensure that Algorand users can benefit from the properties that the UTXO model can provide even though Algorand is using the account model. You can find out more about the difference between the UTXO model and Account model [here](https://www.youtube.com/watch?v=HT6_j_ZyAms).

## Why should you use Unnamed Wallet?

[These privacy and security features](https://github.com/0xLiquidGlass/unnamed/blob/labs-liquidglass/unnamedwallet/src/README.md) in Unnamed Wallet ensures that you have financial privacy and your funds are always safe with you

## What Is It Built On?

[Algorand Python SDK](https://github.com/algorand/py-algorand-sdk)

## Operating System

- Linux (Debian, Fedora)

More Operating Systems and distributions will be added as soon as the necessary dependencies or modifications are written for them

[Requirements](https://github.com/0xLiquidGlass/unnamed/tree/labs-liquidglass#requirements) will explain the requiements on what to install manually to ensure Unnamed Wallet works for you even if your Operating System or distribution is not supported for the installation process

## Requirements

- ["wallet/" directory](https://github.com/0xLiquidGlass/unnamed/tree/labs-liquidglass#making-wallet-directories)
- python3 (or [Python on Windows](https://www.python.org/downloads/))
- [Algorand Python SDK](https://github.com/algorand/py-algorand-sdk) via `pip3 install py-algorand-sdk`
- [pynacl](https://pynacl.readthedocs.io/en/latest/) via `pip install pynacl'

## Making wallet/ directories

### 1. Transactions path

The following code will make the paths for the handling of keypairs for regular transactions:

```
mkdir wallet/ \
      wallet/transaction/ \
      wallet/transaction/spent/ \
      wallet/transaction/unspent/ \
      wallet/transaction/unsafe/ \
```

Note that that is for Unix-like Operating Systems only. For Windows, the command would be:

```
mkdir wallet
mkdir wallet\transaction
mkdir wallet\transaction\spent
mkdir wallet\transaction\unspent
mkdir wallet\transaction\unsafe
```

Paste the code above into the command prompt

## Project Related

The project is currently looking for volunteers to help contribute to Unnamed Wallet. Here are some of the roles that you can apply for:

### 1. Social Network Moderators
- Maintain order for various social networks
- Interact with the Unnamed Wallet community
- PGP optional, but encouraged
- Submit Linkedin or Github profile

### 2. Endowment Managers
- Manage crowdsourcing funds and be a part of the multisig key holder
- Manage endowments
- Must have PGP
- Must be ready to identify yourself
- Submit Linkedin profile

### 3. Marketing
- Reach out to people to raise awareness of Unnamed Wallet
- Find partnerships
- PGP optional, but encouraged
- Submit Linkedin or Github profile

If you are interested in volunteering for the project, please contact 0xLiquidGlass through [any of the contacts listed here](https://github.com/0xLiquidGlass/0xLiquidGlass/blob/main/README.md#contact).

## Socials

- [Discord](https://discord.gg/kePECdcXad)
- [Reddit](https://www.reddit.com/r/unnamed_wallet/)

## Donations

If you support this project, please donate. The proceeds will be used for the development of this project.

``` 
  Algorand: 7VMA5N3QN6EN4DZ5WE4FZB4YTYDLPVELJNPX3GANZ7DMR4DL7YVXKO7WCM
```
