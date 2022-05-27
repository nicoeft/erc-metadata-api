import requests
import json


class EtherscanRepository:
    @staticmethod
    def get_abi(contract_address):
        try:
            response = requests.get(
                f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}"
            )
            return json.loads(response.json()["result"])
        except Exception as e:
            print(e)
            return None
