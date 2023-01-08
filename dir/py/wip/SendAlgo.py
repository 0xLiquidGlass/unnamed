# SendAlgo will use UTXO model to create
# a tx that has multiple input/output 

# Atomic transfers that take multiple unsigned transactions
# and combine them under one group ID so that we can process all of them
# in one combined transaction
# Ref Doc: https://developer.algorand.org/docs/get-details/atomic_transfers/
from algod_utils.algodinstance import algodinstance
import CombineKeypairs
import AssetBalance
from algosdk import mnemonic, account
from algosdk.transaction import *
import os 

def send_algo_from_wallet():
    # get all wallets and list them for user selection
    wallets = CombineKeypairs.query_every_user_wallet()
    print(f'Total wallets: {len(wallets)}')
    AssetBalance.query_total_balance()  # should print wallet and corresponding balance in microalgos
    
    # Receive user input for amount and receiver's address 
    print('Send Algo from: ', end='')
    selection = int(input())    # send algo from 
    sender_wallet = wallets[selection-1]
    account_info = algodinstance().getclient().account_info(sender_wallet)
    print(f'Sending algo from: {sender_wallet} | {account_info["amount"]}')
    print('Amount to send (micro Algos): ', end='')
    amount = int(input())
    # Dont allow amounts greater than current balance
    # this will change once we start aggregating wallets to prepare amount to be sent 
    if(amount > int(account_info["amount"])):
        print(f'Not enough Algos to send. Current balance of this wallet: {account_info["amount"]}')
        return

    print('Receiver Address: ', end='')
    receiver_address = input()
    # @Todo: Validate user inputs
    print(f'Sending {amount} micro Algos to {receiver_address}')
    
    # demo initial tx of algo from one account to the other
    # while this is good and all, refactoring should focus this file first

    # Find the wallet that user selected 
    wallet_files = [filename for filename in os.listdir("../wallets/") if filename.endswith(".txt")]
    sender_sk = None
    for walletfile in wallet_files:
        with open('../wallets/'+walletfile) as wal:
            if(wal.readline().split(':')[1].strip() == sender_wallet):
                wal.readline() # ignore newline 
                sender_sk = mnemonic.to_private_key(wal.readline().split(':')[1].strip())
                break # found the account

    # Send transaction is privatekey for sender_wallet valid
    if(sender_sk != None):
        # Prepare txn parameters, and unsigned txn,
        algo_transfer_params = algodinstance().getclient().suggested_params()
        algo_transfer_txn = PaymentTxn(sender_wallet, algo_transfer_params, receiver_address, amount)
        print(f'Transaction Processing: ID - {algo_transfer_txn.get_txid()}')
        # sign that unsigned tx and send it 
        signed_algo_transfer_txn = algo_transfer_txn.sign(sender_sk)    # sign with sender's private key

        algo_transfer_txn_id = algodinstance().getclient().send_transaction(signed_algo_transfer_txn)
        print(f'Transaction sent: {algo_transfer_txn_id}')

    # Verify balance change
    print('Await Txn for a few seconds')
    input()
    AssetBalance.query_total_balance()

# test basic Algo sending from one account to the other
send_algo_from_wallet()