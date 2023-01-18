# this will provide access and entry point to unnamed wallet

# Notes: Operating wallet is NOT using same derivation path 
# for generating new accounts. all accounts are generated through 
# generate_account() method provided by algosdk.account class 
# Alrand account creation methods ref:
# https://developer.algorand.org/docs/get-details/accounts/create/

# - We use wallet here to create a container that will hold all the 
# accounts created by user either manually or automatically when tx is sent
# - User can have multiple wallets (with walletname as their identifier)
# - And each wallet can contain N accounts beginning from 1 
# (1 when the wallet itself is created)

# Initial page/menu - possible idea 
#############################################################
#                Welcome to Unnamed Wallet                  # 
#                   [Current Wallet]                        #
# [Total_accounts]                    [Total Algo Balance]  #
#############################################################
# 1. Create new wallet (creates new wallet - that will hold subaccounts)
# 2. Select Operating Wallet (select the wallet from list of previously created wallets (if any in local system))
# 3. Create new sub-account (*operating wallet required)
# 4. Print all sub-accounts details (with balances) (*operating wallet required)
# 5. Send Algo (single-receipient-one-new-account) (*operating wallet required)
# 6. Send Algo (single-receipient-multiple-new-accounts) (*operating wallet required)
# 7. Send Algo (multiple-receipients-one-new-account) (*operating wallet required)
# 8. Send Algo (multiple-receivers-multiple-new-accounts) (*operating wallet required)


from walletcore import UnnamedWallet, utils, constants

# @Todo: consider adding console_menu from 
# https://github.com/aegirhall/console-menu
# for better user interaction.
def print_main_wallet_menu():
    print('-------------- Welcome to Unnamed Wallet --------------')
    print('---------- Algorand wallet that mimics utxo -----------')
    print(f'-Active Wallet: {None}')
    print(f'-Total accounts under active wallet: {None}')
    print(f'-Total Algo across all accounts of wallet {None}: {None}')
    print(f'-Total wallets: {None}')
    print(f'-Total Algo across all wallets: {None}')
    print('-------------------------------------------------------')
    pass

def main():
    pass 

if __name__ == '__main__':
    # @Todo: load default wallet once user logs in (if any)
    main()