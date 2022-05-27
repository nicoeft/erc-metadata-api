from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from project.metadata.infraestructure.opensea_repository import OpenseaRepository
from project.metadata.infraestructure.postgres_repository import PostgresRepository
from project.metadata.services.get_metadata import GetMetadata
from project.metadata.services.upsert_metadata import UpsertMetadata


class Metadata(APIView):
    def get(self, request, contract_address, token_id):
        metadata = GetMetadata(contract_address, token_id, OpenseaRepository).execute()
        if not metadata:
            # Fallback to cached
            metadata = GetMetadata(
                contract_address, token_id, PostgresRepository
            ).execute()
            if not metadata:
                # Fallback to blockchain
                metadata = GetMetadata(
                    contract_address, token_id, PostgresRepository
                ).execute()

        if not metadata:
            return Response(
                {"message": "Token not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Update cached metadata
        UpsertMetadata(metadata, PostgresRepository).execute()

        return Response(
            status=status.HTTP_200_OK,
            data=metadata,
        )
