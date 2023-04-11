from globals.AlgodUtils import algodClient
import os

asaDatabase = "AddedAssets.csv"


def add_asa(assetId):
        assetInfo = algodClient.asset_info(assetId)
        assetParams = assetInfo["Params"]
        assetName = assetParams["name"]
        existInDatabaseStatus = check_if_id_in_database(assetId)
        if existInDatabaseStatus == int(1):
                print("\nThis asset exists in the databse")
        elif existInDatabaseStatus == int(0):
                print("\nWriting {} to database" .format(assetId))
                with open(asaDatabase, "a") as writeAssetDatabase:
                        writeAssetDatabase.write("{},{}" .format(assetName, assetId))

def check_if_id_in_database(assetId):
        try:
                with open(asaDatabase, "r") as readAssetDatabase:
                        databaseContents = readAssetDatabase.read()
                        if assetId in databaseContents:
                                return int(1)
                        else:
                                return int(0)

        except FileNotFoundError:
                return int(0)

def remove_asa(assetName):
