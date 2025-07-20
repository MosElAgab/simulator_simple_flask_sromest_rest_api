import requests

class QueryBase:
    def __init__(self, base_url: str, authorization_header: dict):
        self.base_url = base_url
        self.authorization_header = authorization_header

    # TODO: add logic for when api call fails
    def get_stores(self) -> dict:
        # TODO: should retrun an empty list and logs failed response
        response = requests.get(f"{self.base_url}/store")
        return response.json()


    def get_store_ids(self, stores: list) -> list:
        store_ids = [store["store_id"] for store in stores]
        return store_ids
