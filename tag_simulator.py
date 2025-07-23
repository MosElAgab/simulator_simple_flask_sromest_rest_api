import random
import requests
from faker import Faker

from query_base import QueryBase

faker = Faker()


class TagSimulator(QueryBase):
    
    def create_tag_data(self) -> dict:
        tag_name = "-".join(faker.words(nb=2))
        data = {
            "tag_name": tag_name
        }
        return data
    

    def create_tag(self, tag_data: dict) -> dict:
        stores = self.get_stores()
        store_id = random.choice(self.get_store_ids(stores))
        response = requests.post(
            f"{self.base_url}/store/{store_id}/tag",
            json=tag_data,
            headers=self.authorization_header
        )
        if response.ok:
            print("Create tag:", response.status_code, response.json())
        else:
            print("Failed:", response.status_code, response.json())
        return response.json()
    

    def create_many_tags(self, number_of_tags: int) -> None:
        # TODO: Retrun created tags
        for i in range(number_of_tags):
            tag_data = self.create_tag_data()
            self.create_tag(tag_data)
