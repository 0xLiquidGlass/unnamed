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

# Active wallet intance should handle all sub-account related actions
# unnamedWallet object
active_wallet = None 
# @Todo: consider adding console_menu from 
# https://github.com/aegirhall/console-menu
# for better user interaction.
def print_main_wallet_menu():
    global active_wallet
    print('-------------- Welcome to Unnamed Wallet --------------')
    print('---------- Algorand wallet that mimics utxo -----------')
    print(f'-Active Wallet: {active_wallet.wallet if active_wallet else None}')
    print(f'-Total accounts under {active_wallet.wallet if active_wallet else None} wallet: {str(active_wallet.total_accounts) if active_wallet else None}')
    print(f'-Total Algo across all accounts in wallet {active_wallet.wallet if active_wallet else None}: {str(active_wallet.total_algo_balance_of_active_wallet()) if active_wallet else None}')
    print(f'-Total wallets: {str(UnnamedWallet.total_wallets())}')
    print(f'-Total Algo across all wallets: {None}')
    print('-------------------------------------------------------')
    print('1. Create New Wallet (container for sub-accounts)')
    print('2. Select Operating Wallet')
    print(f'3. Create New Sub-Account {("under:" + active_wallet.wallet) if active_wallet else ""}')
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
    # If no active wallet present, select recently created as active one
    if(active_wallet is None):
        active_wallet = UnnamedWallet(wallet_name)
    else:
        UnnamedWallet(wallet_name)

def handle_sel_2_new_wallet():
    pass
def handle_sel_3_new_wallet():
    pass
def handle_sel_4_new_wallet():
    pass
def handle_sel_5_new_wallet():
    pass
def handle_sel_6_new_wallet():
    pass
def handle_sel_7_new_wallet():
    pass
def handle_sel_8_new_wallet():
    pass
def handle_sel_9_new_wallet():
    pass

# To handle menu interactions
def handle_menu_selection(user_selection: int, limited: bool = True):
    # active wallet not present, don't allow Algo send options without an active wallet
    if limited == True:
        # Check if user_selection within 1 to 5, if not indicate "wallet selection required"
        if(user_selection < 1 or user_selection > 5):
            # Select active wallet first
            print('Select an active wallet first.\n')
            return
    
    # As limited menu option selection is verified above
    # control only comes here if one of following is true  
    # limited is False (active_wallet present, allow user to perform all actions)
    # limited is True, user_selection is within range 

    # dispatch handler - associated function call dispatch using dictionary
    # https://stackoverflow.com/questions/9205081/is-there-a-way-to-store-a-function-in-a-list-or-dictionary-so-that-when-the-inde
    function_call_dispatcher = {
        1: handle_sel_1_new_wallet,
        2: handle_sel_2_new_wallet,
        3: handle_sel_3_new_wallet,
        4: handle_sel_4_new_wallet,
        5: handle_sel_5_new_wallet,
        6: handle_sel_6_new_wallet,
        7: handle_sel_7_new_wallet,
        8: handle_sel_8_new_wallet,
        9: handle_sel_9_new_wallet,
    }
    
    # Call related functions to handle interaction 
    # This can throw - key not found, as we haven't verified whether 
    # user input was within 1 and 10. We don't need to actually, if it throws,
    # main will handle the case and "invalid input - please add correct input" (@Todo: verify)
    function_call_dispatcher[user_selection]()
    


# Handle unnamed wallet init
# Check if any wallet can be loaded while initializing 
# load up the default wallet 
def init_wallet():
    pass


def main():
    # init_wallet()
    while(True):
        print_main_wallet_menu()
        user_selection = input()
        try:
            # Handle program exit condition first
            if(int(user_selection) == 10):
                print("Exiting unnamed wallet...\n\n")
                break
            # If active_wallet is not present, only allow certain options to be selected
            # indicated by where to show menu in limited accessibility form
            if(active_wallet):
                handle_menu_selection(int(user_selection), limited=False)
            else: 
                handle_menu_selection(int(user_selection), limited=True)
        except:
            print('Invalid Input. Please enter correct selection.\n\n')
            continue

if __name__ == '__main__':
    # @Todo: load default wallet once user logs in (if any)
    main()