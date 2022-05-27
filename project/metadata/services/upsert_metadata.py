class UpsertMetadata:
    def __init__(self, data, repository):
        self.data = data
        self.repository = repository

    def execute(self):
        return self.repository.upsert_metadata(self.data)
