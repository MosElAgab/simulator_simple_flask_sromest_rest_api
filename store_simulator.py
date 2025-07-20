import uuid
import requests
from faker import Faker

faker = Faker()

class StoreSimulator:

    def __init__(self, base_url: str, authorization_header: dict):
        self.base_url = base_url
        self.authorization_header = authorization_header


    def get_stores(self) -> list:
        response = requests.get(f"{self.base_url}/store")
        return response.json()


    def get_store_ids(self, stores: list) -> list:
        store_ids = [store["store_id"] for store in stores]
        return store_ids


    def create_store_data(self) -> dict:
        store_name = faker.company() + "-" + uuid.uuid4().hex[0:2]
        data = {
            "store_name": store_name
        }
        return data


    def create_store(self, store_data: dict) -> dict:
        response = requests.post(f"{self.base_url}/store", json=store_data, headers=self.authorization_header)
        if response.ok:
            print("Create store:", response.status_code, response.json())
        else:
            print("Failed:", response.status_code, response.json())

        return response.json()


    def create_many_stores(self, number_of_store: int) -> None:
        # TODO: return created stores.
        for i in range(number_of_store):
            store_data = self.create_store_data()
            self.create_store(store_data)
