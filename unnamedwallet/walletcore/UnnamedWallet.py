# Basic functionality
# Allow user to create wallets - subaccounts 
# Allow user to receive/send algo from those wallets/subaccounts

from algosdk import account, mnemonic
from walletcore import constants
from walletcore.utils import algodinstance
import os 
from dotenv import load_dotenv
load_dotenv()


class UnnamedWallet:
    
    def __init__(self, walletname: str):
        self._wallet = walletname
        self._total_accounts = 0
        self.generate_new_account()
        print(f'New wallet {walletname} has been generated.\n\n')

    @property
    def wallet(self) -> str:
        return self._wallet

    @property
    def total_accounts(self) -> int:
        return self._total_accounts


    """
    This static method is responsible to count total number 
    of wallets present locally 
    """
    @staticmethod
    def total_wallets() -> int:
        # Get all present wallets
        wallet_files = [filename for filename in os.listdir("./walletcore/wallets/") if filename.endswith(".txt")]
        return len(wallet_files)    # can be 0 if no wallet has been created yet


    """
    Static method to handle total algo present across all wallets

    """
    @staticmethod
    def total_algo_across_all_wallets() -> int:
        pass


    """
    Create new sub_account [Contained within this wallet] in /wallets/,
    This can either be used as output wallet that
    receives remaining funds (as per user's selection on how
    this distribution should happen)
    Note: This was handled by GenerateWallet.py
    """
    def generate_new_account(self):
        # account name as [walletname]_[accountnumber]
        account_name = self.wallet + "_" + str(self.total_accounts + 1)
        # create the wallet file as txt, and add pub key and seed to the file
        # @Todo: change these plaintexts to ECIES
        with open(os.path.dirname(__file__)  + "/wallets/" + account_name + ".txt", "x") as wallet_file:
            private_key, address = account.generate_account()
            self._total_accounts += 1
            wallet_file.write("Address: {}\n\n" .format(address))
            wallet_file.write("Seed: {}" .format(mnemonic.from_private_key(private_key)))
		

    """
    Returns a list of all accounts generated within wallet and
    Note: This was handled by CombineKeypairs.py previously
    """
    def get_all_accounts_in_current_active_wallet(self) -> list:
        # Get all present wallets + check if wallet name is matching with current active wallet 
        wallet_files = [filename for filename in (os.path.dirname(__file__) + "/wallets/") if filename.endswith(".txt") and self.wallet in filename]
        # list of wallet addresses
        accounts = []
        for wallet in wallet_files:
            # open that wallet file and read address line
            with open(os.path.dirname(__file__) + '/wallets/' + wallet) as wal:
                accounts.append(wal.readline().split(':')[1].strip())	# pub address
        return accounts # can be empty list if no wallets created yet 


    """
    Total user balance in Algo (In Active Wallet)
    Counts algo from all the sub-accounts present in /wallets/
    print_details: if we want to print all subaccounts with their respective balances while 
    calculating the total balance
    returns: balance in microalgo
    """
    def total_algo_balance_of_active_wallet(self, print_details: bool = False) -> int:
        total_mAlgo_balance = 0
        algod_client = algodinstance.algodinstance().getclient()
        all_wallets = self.get_all_accounts_in_current_active_wallet()   # list of all subaccounts present under wallet
        if(print_details == True):
            print(f'Total sub-accounts - {len(all_wallets)}')
        
        # get account_info() for every account present in /wallets/ dir 
        for i in range(len(all_wallets)):
            account_info = algod_client.account_info(all_wallets[i])
            total_mAlgo_balance += account_info.get("amount")
            # Print details about the account and algo balance
            if(print_details == True):
                print(f'Account-{i+1}: {all_wallets[i]} | Balance: {str(int(account_info.get("amount"))/constants.MICROALGOS_TO_ALGOS_RATIO)} Algo')

        return total_mAlgo_balance


    """
    Prints the list of accounts available and their balances
    """
    def print_all_balances(self):
        total_mAlgo_balance = self.total_algo_balance(print_details=True)
        print ("Balance: {:.2f} Algos" . format(total_mAlgo_balance/constants.MICROALGOS_TO_ALGOS_RATIO))


    """
    Send algo to one receiver, 
    remaining funds will be sent to a new account
    """
    def send_algo_to_receiver(self, receiver_address: str):
        pass 


    """
    Send algos to list of receivers,
    remaining funds to new account(s)
    """
    def self_algo_to_list_of_receivers(self, receives_distribution: dict):
        pass 


    """
    Prepare atomic transaction that will be submitted to Algo network
    At max 16 tx can be included 
    """
    def prepare_atomic_transaction(self, transactions: list):
        pass 


    def __repr__(self) -> str:
        pass