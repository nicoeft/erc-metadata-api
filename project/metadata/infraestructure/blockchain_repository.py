import requests

from project.metadata.infraestructure.etherscan_repository import EtherscanRepository
from project.metadata.services.get_smart_contract_abi import GetSmartContractABI
from web3 import Web3
from web3.auto.infura import w3


class BlockchainRepository:
    @staticmethod
    def get_metadata(contract_address, token_id):
        abi = GetSmartContractABI(contract_address, EtherscanRepository).execute()
        contract = w3.eth.contract(
            address=Web3.toChecksumAddress(contract_address), abi=abi
        )
        try:
            decimals = contract.functions.decimals().call()
            contract_name = contract.functions.name().call()
            symbol = contract.functions.symbol().call()
        except Exception as e:
            print(e)
            return None
        else:
            return {
                "name": f"#{token_id}",
                "category": None,
                "decimals": decimals,
                "contract_name": contract_name,
                "symbol": symbol,
                "is_verified": None,
            }
