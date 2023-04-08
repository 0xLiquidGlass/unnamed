# Unnamed - An Algorand Wallet That Mimics UTXO

## Introduction

Unnamed wallet is built with mainly privacy, and security in mind. The project was originally thought of as a solution to combat successful attempts on phishing attacks by leveraging Public Key Cryptography, which all cryptocurrency wallet uses.

Unnamed wallet mimics Unspent Transaction Outputs, or UTXO for short. This is the model used by Bitcoin to solve the double spending problem by not reusing the same address twice after the address has been spent. The wallet will use the properties of privacy and security present in UTXO without using the Algorand blockchain to ensure that Algorand users can benefit from the properties that the UTXO model can provide even though Algorand is using the account model. You can find out more about the difference between the UTXO model and Account model [here](https://www.youtube.com/watch?v=HT6_j_ZyAms).

## Why should you use Unnamed Wallet?

[These privacy and security features](https://github.com/0xLiquidGlass/unnamed/blob/labs-liquidglass/unnamedwallet/src/README.md) in Unnamed Wallet ensures that you have financial privacy and your funds are always safe with you

## What Is It Built On?

[Algorand Python SDK](https://github.com/algorand/py-algorand-sdk)

## Operating System (Full Functionality)

- Linux (Debian, Fedora)
<<<<<<< HEAD
- Windows
=======
>>>>>>> 62c52b194097b9123dab883c3ef9b5d4049ac7df

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

## Updates And Upgrades

### 1. To update or upgrade Unnamed Wallet:

- Extract the archived app and go into the first directory

- Cut or copy all of the files and directories in the directory with the new version

- Paste all of the files that was cut or copied from the directory containing the new version of Unnamed Wallet into the directory of the current wallet that you are using

- Overwrite all of the files when prompted

### 2. To make sure that you are getting the correct software:

- Get GPG [here for Windows users](https://gnupg.org/download/index.html) or if you are using Linux or BSD, make sure your distribution has `gpg` installed by running `gpg --version`

- For Windows users, you may want to use Kleopatra, as it will be easier to use rather than the `gpg` command

- Download the .asc file from releases. Make sure the file you are downloading is for the correct operating system (e.g. unnamedwallet-linux.tar.gz will be unnamedwallet-linux.tar.gz.asc)

- Get the PGP public key from the `#pgp-keys` channel in [Unnamed Wallet's Discord server](https://discord.gg/kePECdcXad)

- As of v1.0.0, 0xLiquidGlass `(PGP Fingerprint: 7C7B A828 4F67 3865 A4B7 9FD2 2957 408A B3BB 6E56)` signs the release

- For import the public key to GPG

- For Windows users, click on `Decrypt/Verify` and select the .asc file

- For Command Line Interface users, do `gpg --verify /path/to/asc-file/`. Note that `asc-file` refers to the name of the .asc file that  you just downloaded

- The PGP Fingerprint should show the correct fingerprint. If not, the software is either corrupted, tampered with, or malicious

- Your .asc file and the app must be in the same directory

### 3. To check the file using sha256sum

- Download the .sha256 file from releases

- For Windows, use apps like [7zip](https://www.7-zip.org/download.html) to verify your sha256 checksum easily

- For Linux users, use sha256sum to verify the checksum of your app using the .sha256 file

- Your .sha256 file and the app must be in the same directory

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
