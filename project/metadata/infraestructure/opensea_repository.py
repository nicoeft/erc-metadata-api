import os

import requests

OPENSEA_API_KEY = os.environ.get("OPENSEA_API_KEY")


class OpenseaRepository:
    @staticmethod
    def get_metadata(contract_address, token_id):
        try:
            url = f"https://api.opensea.io/api/v1/asset/{contract_address}/{token_id}/?include_orders=false"
            response = requests.get(url, headers={"X-API-KEY": OPENSEA_API_KEY})
            if not response.ok:
                return None
            data = response.json()
        except Exception as e:
            print(e)
            return None
        else:
            contract = data["asset_contract"]
            return {
                "name": data.get("name", f"#{token_id}"),
                "category": contract.get("category"),
                "decimals": data.get("decimals"),
                "thumbnail_url": data.get("image_thumbnail_url"),
                "animation_url": data.get("animation_url"),
                "contract_name": contract.get("name"),
                "symbol": contract.get("symbol"),
                "is_verified": data.get("collection", {}).get(
                    "safelist_request_status", False
                ),
            }
