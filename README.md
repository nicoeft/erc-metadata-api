# DRF ERC Token Metadata API

Simple Django app to fetch metadata from ERC721/ERC1155 tokens using [OpenSea](https://docs.opensea.io/reference/api-overview) API
with fallbacks to db if API is not available and fallback to smart contract if token never stored in db.

Environment variables needed in .env file:
```
WEB3_INFURA_PROJECT_ID
DATABASE_URL
OPENSEA_API_KEY
```

Start server locally:
```
python manage.py runserver
```

Endpoints:
`http://127.0.0.1:8000/api/v1/metadata/<contract_addres>/<token_id>/`



