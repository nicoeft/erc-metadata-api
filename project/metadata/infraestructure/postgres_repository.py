import requests
import json

from project.metadata.models import Metadata, SmartContract


class PostgresRepository:
    @staticmethod
    def get_metadata(contract_address, token_id):
        try:
            metadata = Metadata.objects.get(
                smart_contract=contract_address, token_id=token_id
            )
        except Metadata.DoesNotExist:
            return None
        else:
            return {
                "name": metadata.name,
                "category": metadata.smart_contract.category,
                "decimals": metadata.smart_contract.decimals,
                "thumbnail_url": metadata.thumbnail_url,
                "animation_url": metadata.animation_url,
                "contract_name": metadata.smart_contract.name,
                "symbol": metadata.smart_contract.symbol,
                "is_verified": None,
            }

    @staticmethod
    def upsert_metadata(data):
        smart_contract, _created = SmartContract.objects.update_or_create(
            address=data["contract_address"],
            defaults={
                "name": data.get("contract_name"),
                "symbol": data.get("symbol"),
                "category": data.get("category"),
                "decimals": data.get("decimals"),
                "abi": data.get("abi"),
            },
        )
        Metadata.objects.update_or_create(
            smart_contract=smart_contract,
            token_id=data.get("token_id"),
            defaults={
                "name": data.get("name"),
                "thumbnail_url": data.get("thumbnail_url"),
                "animation_url": data.get("animation_url"),
                "is_verified": data.get("is_verified"),
            },
        )
