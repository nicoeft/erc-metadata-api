class GetMetadata:
    def __init__(self, contract_address, token_id, repository):
        self.contract_address = contract_address
        self.token_id = token_id
        self.repository = repository

    def execute(self):
        return self.repository.get_metadata(self.contract_address, self.token_id)
