"""
Written by Liquid Glass

This program is meant for Windows NT (desktop) use

By using this program, you are able to easily interface with the individual
functions of Unnamed Wallet without having to look through the src/ directory
to find what you want to do and executing it manually
"""

import os
import subprocess

def clear_screen():
        os.system("cls")

def continue_message():
        str(input("\nPress enter to continue"))

def end_message():
        str(input("\nDone. Press enter to continue"))

def try_again_message():
        print("Please try again\n")

def run_process(listOfCommands):
        returnCode = subprocess.call(listOfCommands, shell = False)

        if returnCode == 0:
                print("\nCompleted")
        else:
                print("\nPython error code: {}".format(returnCode))

def initiate_shutdown_stuff():
        clear_screen()
        exit(0)

def greeter_stuff():
        clear_screen()
        print("Welcome to Unnamed Wallet\n")

def main_mode():
        while True:
                print("\n1 --> Setup")
                print("\n2 --> Make a keyfile")
                print("\n3 --> Generate a new wallet")
                print("\n4 --> Check Algo balance")
                print("\n5 --> Consolidate UTXO balance")
                print("\n6 --> Send Algos to others")
                print("\n7 --> Import your old wallet and sweep")
                print("\n8 --> More options")
                print("\n9 --> Quit\n")

                simpleChoice = str(input("\nYour choice: "))

                if simpleChoice == str(1):
                        clear_screen()
                        dependency_stuff()
                        clear_screen()

                elif simpleChoice == str(2):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "MakeKeyfile.py"])
                        os.chdir("../")
                        continue_message()
                        clear_screen()

                elif simpleChoice == str(3):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "GenerateWallet.py"])
                        os.chdir("../")
                        continue_message()
                        clear_screen()

                elif simpleChoice == str(4):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "AssetBalance.py"])
                        os.chdir("../")
                        continue_message()
                        clear_screen()

                elif simpleChoice == str(5):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "ConsolidateWalletBalance.py"])
                        os.chdir("../")
                        end_message()
                        clear_screen()

                elif simpleChoice == str(6):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "SendAlgo.py"])
                        os.chdir("../")
                        end_message()
                        clear_screen()

                elif simpleChoice == str(7):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "ImportAndSweep.py"])
                        os.chdir("../")
                        end_message()
                        clear_screen()

                elif simpleChoice == str(8):
                        clear_screen()
                        more_options_mode()
                        clear_screen()

                elif simpleChoice == str(9):
                        initiate_shutdown_stuff()

                else:
                        clear_screen()
                        try_again_message()

def dependency_stuff():
        clear_screen()
        os.chdir("src/dependencies")
        run_process(["WindowsNtPackages.bat"])
        os.chdir("../../")
        end_message()

def more_options_mode():
        print("More options\n")
        while True:
                print("\n1 --> Check if an address is valid")
                print("\n2 --> Show previously generated unused addresses")
                print("\n3 --> Go back\n")

                moreChoice = str(input("\nYour Choice: "))

                if moreChoice == str(1):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "ValidateAddress.py"])
                        os.chdir("../")
                        continue_message()
                        clear_screen()

                elif moreChoice == str(2):
                        clear_screen()
                        os.chdir("src/")
                        run_process(["python", "ListUnusedUtxos.py"])
                        os.chdir("../")
                        continue_message()
                        clear_screen()

                elif moreChoice == str(3):
                        break

                else:
                        clear_screen()
                        try_again_message()

if __name__ == "__main__":
        try:
                greeter_stuff()
                main_mode()

        except KeyboardInterrupt:
                initiate_shutdown_stuff()

        except EOFError:
                initiate_shutdown_stuff()
