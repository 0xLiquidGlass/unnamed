# Basic functionality
# Allow user to create wallets - subaccounts 
# Allow user to receive/send algo from those wallets/subaccounts

from algosdk import account, mnemonic
from . import utils
from walletcore import constants
import os 
from dotenv import load_dotenv
load_dotenv()


class UnnamedWallet:
    
    def __init__(self, walletname: str):
        self._wallet = walletname
        self._total_accounts = 0
        self.generate_new_account()
        print(f'New wallet {walletname} has been generated.')

    @property
    def wallet(self) -> str:
        return self._wallet

    @property
    def total_accounts(self) -> int:
        return self._total_accounts

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
    def get_all_accounts(self) -> list:
        # Get all present wallets
        wallet_files = [filename for filename in os.listdir("./wallets/") if filename.endswith(".txt")]\
        # list of wallet addresses
        wallet_addresses = []
        for wallet in wallet_files:
            # open that wallet file and read address line
            with open('../wallets/'+wallet) as wal:
                wallet_addresses.append(wal.readline().split(':')[1].strip())	# pub address
        return wallet_addresses # can be empty list if no wallets created yet

    """
    Total user balance in Algo
    Counts algo from all the sub-accounts present in /wallets/
    print_details: if we want to print all subaccounts with their respective balances while 
    calculating the total balance
    returns: balance in microalgo
    """
    def total_algo_balance(self, print_details: bool = False) -> int:
        total_mAlgo_balance = 0
        algod_client = utils.algodinstance().getclient()
        all_wallets = self.get_all_accounts()
        if(print_details):
            print(f'Total sub-accounts - {len(all_wallets)}')
        
        # get account_info() for every account present in /wallets/ dir 
        for i in range(len(all_wallets)):
            account_info = algod_client.account_info(all_wallets[i])
            total_mAlgo_balance += account_info.get("amount")
            # Print details about the account and algo balance
            if(print_details):
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