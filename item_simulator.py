import uuid
import requests
import random
from faker import Faker

faker = Faker()

class ItemSimulator:
    
    def __init__(self, base_url, authorization_header):
        self.base_url = base_url
        self.authorization_header = authorization_header


    def get_stores(self):
        response = requests.get(f"{self.base_url}/store")
        return response.json()


    def get_store_ids(self, stores):
        store_ids = [store["store_id"] for store in stores]
        return store_ids
    

    def create_item_data(self, price_range: set):
        stores = self.get_stores()
        store_id = random.choice(self.get_store_ids(stores))
        item_name = faker.unique.word()
        item_price = round(random.uniform(*price_range), 2)
        data = {
            "item_name": item_name,
            "item_price": item_price,
            "store_id": store_id
        }
        return data


    def create_item(self, item_data):
        response = requests.post(f"{self.base_url}/item", json=item_data, headers=self.authorization_header)
        if response.ok:
            print("Create item:", response.status_code, response.json())
        else:
            print("Failed:", response.status_code, response.json())

        return response.json()


    def create_many_items(self, number_of_items, price_range: set):
        for i in range(number_of_items):
            item_data= self.create_item_data(price_range)
            self.create_item(item_data)
