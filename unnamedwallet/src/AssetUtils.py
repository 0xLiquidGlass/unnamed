"""
Written by Liquid Glass

Useable functions whne imported:

1. add_asset(asaId)

2. remove_asset(asaName)

"""

from globals.FileNameExtensions import tempFileExtension
from globals.FilePaths import asaIdDatabasePath
from globals.AlgodUtils import algodClient
import os

def add_asa(asaId):
        asaInfo = algodClient.asset_info(asaId)
        asaName = asaInfo["params"]["name"]
        # For testing
        # print(asaName)
        with open(asaIdDatabasePath, "a") as addAsaIdPath:
                addAsaIdPath.write("{}: {}" .format(asaName, asaInfo))

def remove_asa(assetName):
        with open(assetIdDatabasePath) as readFile:
                for assetDatabaseLine in readFile:
                        rewrite_asset_database(assetName, assetDatabaseLine)

def rewrite_asa_database(asaName, asaDatabaseLine):
        asaKeyword = asaName
        if asaKeyword not in asaDatabaseLine:
                tempAsaDatabase = asaIdDatabasePath + tempFileExtension
                with open(tempAsaDatabase, "w") as newAsaDatabase:
                        newTempAsaDatabase.write(asaDatabaseLine)
        os.replace(newAsaDatabase, assetIdDatabasePath)

if __name__ == "__main__":
        # For testing
        while True:
                try:
                        asaId = int(input("Asset ID: "))
                        add_asa(asaId)
                        break

                except KeyboardInterrupt:
                        exit(0)

                except:
                        print("\nSomething went wrong")
                        print("\nPlease try again")
