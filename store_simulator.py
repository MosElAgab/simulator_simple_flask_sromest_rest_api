import uuid
import requests
from faker import Faker

from query_base import QueryBase

faker = Faker()

class StoreSimulator(QueryBase):

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


    def create_many_stores(self, number_of_stores: int) -> None:
        # TODO: return created stores.
        for i in range(number_of_stores):
            store_data = self.create_store_data()
            self.create_store(store_data)
