class GetSmartContractABI:
    def __init__(self, contract_address, abi_repository):
        self.contract_address = contract_address
        self.abi_repository = abi_repository

    def execute(self):
        return self.abi_repository.get_abi(self.contract_address)
