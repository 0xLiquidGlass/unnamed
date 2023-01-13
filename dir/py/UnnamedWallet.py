# Basic functionality
# Allow user to create wallets - subaccounts 
# Allow user to receive/send algo from those wallets/subaccounts

from algosdk import account, mnemonic
import os 
from dotenv import load_dotenv
load_dotenv()


class UnnamedWallet:
    
    def __init__(self, walletname):
        self._wallet = walletname

    @property
    def wallet(self):
        return self._wallet

    """
    Create new sub_account [Contained within this wallet],
    This can either be used as output wallet that
    receives remaining funds (as per user's selection on how
    this distribution should happen)
    """
    def generate_new_account(self):
        pass 
    
    """
    Total user balance in Algo
    Counts algo from all the sub-accounts present in /wallets/
    """
    def total_balance(self):
        pass

    """
    Total user balance in Algo
    Counts algo from all the sub-accounts present in /wallets/
    """
    def total_balance(self):
        pass

    """
    Send algo to one receiver, 
    remaining funds will be sent to a new account
    """
    def send_algo_to_receiver(self, receiver_address):
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