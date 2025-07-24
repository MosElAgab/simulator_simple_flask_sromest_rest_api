import os
import requests
from dotenv import load_dotenv

from store_simulator import StoreSimulator
from item_simulator import ItemSimulator
from tag_simulator import TagSimulator

load_dotenv()

# TODO: add create_user

def create_user(username, password):
    user_data = {
        "username": username,
        "password": password
    }
    response = requests.post(f"{base_url}/register", json=user_data)

    if not response.ok:
        raise RuntimeError(f"User register failed: {response.status_code} - {response.text}")
    elif response.ok:
        print("Registered successfully")
    
    return response.json()


def login(username, password):
    login_data = {
        "username": username,
        "password": password
    }

    response = requests.post(f"{base_url}/login", json=login_data)
    if not response.ok:
        raise RuntimeError(f"Login failed: {response.status_code} - {response.text}")
    elif response.ok:
        print("logged in successfully")

    access_token = response.json().get("access_token")
    if not access_token:
        raise ValueError("Access token error.")

    authorization_header = {"Authorization": f"Bearer {access_token}"}
    return authorization_header


base_url = os.getenv("BASE_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
if not username or not password:
    raise ValueError("USERNAME or PASSWORD not set.")

try:
        create_user(username, password)
except RuntimeError as e:
    print(e)

authorization_header = login(username, password)
store_simulator = StoreSimulator(base_url, authorization_header)
item_simulator = ItemSimulator(base_url, authorization_header)
tag_simulator = TagSimulator(base_url, authorization_header)

number_of_stores = 10
number_of_items = 10
items_price_range = (10, 250)
number_of_tags = 10

if __name__ == "__main__":
    store_simulator.create_many_stores(number_of_stores)
    item_simulator.create_many_items(number_of_items, items_price_range)
    tag_simulator.create_many_tags(number_of_tags)
