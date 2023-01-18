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


from walletcore import utils, constants
from walletcore.UnnamedWallet import UnnamedWallet

active_wallet = None 
# @Todo: consider adding console_menu from 
# https://github.com/aegirhall/console-menu
# for better user interaction.
def print_main_wallet_menu():
    global active_wallet
    print('-------------- Welcome to Unnamed Wallet --------------')
    print('---------- Algorand wallet that mimics utxo -----------')
    print(f'-Active Wallet: {active_wallet}')
    print(f'-Total accounts under {active_wallet} wallet: {None}')
    print(f'-Total Algo across all accounts in wallet {active_wallet}: {None}')
    print(f'-Total wallets: {None}')
    print(f'-Total Algo across all wallets: {None}')
    print('-------------------------------------------------------')
    print('1. Create New Wallet (container for sub-accounts)')
    print('2. Select Operating Wallet')
    print(f'3. Create New Sub-Account {("under:" + active_wallet) if active_wallet else ""}')
    print('4. Print all sub-accounts balances')
    print('5. Receive Algo') # Display all accounts - and select one to receive Algo to
    # Send specified amount of Algo to someone, and send remaining funds to a new account
    print('6. Send Algo (single-receipient-single-new-account') 
    # Send specified amount of Algo to someone, and send remaining funds to multiple new accounts
    # Allow user to choose size of new accounts + single account handling all tx fees +
    # maintain minimum algo requirement before sending 
    print('7. Send Algo (single-receipient-multiple-new-accounts')
    # This is where we might need to add better UI - to visulize txs across multiple sub-accounts
    # These sub-accounts are treated as utxo 
    # (input utxo for Send Algo tx) OR (output utxo when tx happens and new accounts are created)
    print('8. Send Algo (multiple-receipients-single-new-account') # Aggregate back to single account  
    print('9. Send Algo (multiple-receipients-multiple-new-accounts')      
    print('10. Exit')  
    print('-------------------------------------------------------')
    print('Enter your selection: ')

# Defining selection 1 - Creating a new wallet (creates one sub-account)
# Create new wallet - set newly created wallet as active wallet 
# active wallet should only be changed if one hasn't been selected yet 
def handle_sel_1_new_wallet():
    global active_wallet
    print("Enter new wallet name: ", end='')
    wallet_name = input()
    wallet = UnnamedWallet(wallet_name)
    if(active_wallet is None):
        active_wallet = wallet.wallet



def main():
    while(True):
        print_main_wallet_menu()
        user_selection = input()
        try:
            # @Todo: next refactoring should remove this complex nested if.else
            if(active_wallet):
                pass # All options are selectable 
            else: 
                # Exit condition
                if(int(user_selection) == 10):
                    break
                # Only create new wallet, select new active wallet, 
                if(1 <= int(user_selection) <= 5):
                    if int(user_selection) == 1:
                        handle_sel_1_new_wallet()
                    # perform related actions 
                    continue
                else: 
                    # Select active wallet first
                    print('Select an active wallet first.')
                    continue
        except:
            print('Invalid Input. Please enter correct selection: ')
            continue
    print('Exiting unnamed wallet...')

if __name__ == '__main__':
    # @Todo: load default wallet once user logs in (if any)
    # main()
    handle_sel_1_new_wallet()