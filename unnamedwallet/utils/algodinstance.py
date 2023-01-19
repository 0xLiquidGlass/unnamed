# Keep one instance of algod client 
# every other instantiation should yield the same reference 
from algosdk.v2client import algod
import os 

class algodinstance(object):
    _instance = None
    _algo_client = None

    def __new__(algodclass):
        # if there exists no algodClient instance, create one 
        if algodclass._instance is None:
            algodclass._instance = super(algodinstance, algodclass).__new__(algodclass)
            algodclass._algo_client = algod.AlgodClient(os.getenv("ALGOD_TOKEN"), os.getenv("ALGOD_ADDRESS"))
        return algodinstance._instance

    def getclient(self):
        return self._algo_client