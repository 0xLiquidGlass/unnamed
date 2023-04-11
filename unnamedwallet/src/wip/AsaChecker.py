"""
Written by Liquid Glass
"""

from globals.AlgodUtils import algodClient

def check_asa(assetId):
        assetInfo = algodClient.asset_info(assetId)
        assetParams = assetInfo["params"]
        print("\n\nAsset name: {}" .format(assetParams["name"]))
        print("\nAsset properties: {}" .format(list(assetParams.keys())))

if __name__ == "__main__":
        while True:
                try:
                        assetId = int(input("\n\nAsset ID: "))
                        check_asa(assetId)

                except ValueError:
                        print("\nMust be the correct ID")
                        print("\nPlease try again")

                except TypeError:
                        print("\nThe Asset ID must be a number (e.g. USDC is {})" 
                              .format(str(10458941)))
                        print("\nPlease try again")
