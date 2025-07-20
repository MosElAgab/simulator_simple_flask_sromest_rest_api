import uuid
import requests
from faker import Faker

faker = Faker()

class StoreSimulator():

    def __init__(self, base_url, authorization_header):
        self.base_url = base_url
        self.authorization_header = authorization_header


    def create_store_data(self):
        store_name = faker.company() + "-" + uuid.uuid4().hex[0:2]
        data = {
            "store_name": store_name
        }
        return data


    def create_store(self, store_data):
        response = requests.post(f"{self.base_url}/store", json=store_data, headers=self.authorization_header)
        if response.ok:
            print("Create store:", response.status_code, response.json())
        else:
            print("Failed:", response.status_code, response.json())

        return response.json()


    def create_many_stores(self, number_of_store):
        for i in range(number_of_store):
            store_data = self.create_store_data()
            self.create_store(store_data)


    def get_stores(self):
        response = requests.get(f"{self.base_url}/store")
        return response.json()


    def get_store_ids(self, stores):
        store_ids = [store["store_id"] for store in stores]
        return store_ids
