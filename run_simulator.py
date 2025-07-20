import os
import requests
from dotenv import load_dotenv

from store_simulator import StoreSimulator
from item_simulator import ItemSimulator

load_dotenv()

def login(username, password):
    # TODO: add error handling
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

authorization_header = login(username, password)
store_simulator = StoreSimulator(base_url, authorization_header)
item_simulator = ItemSimulator(base_url, authorization_header)

# store_simulator.create_many_stores(5)
# stores = item_simulator.get_stores()
# ids = item_simulator.get_store_ids(stores)

# print(ids)

# print("choice")
# item = item_simulator.create_item_data((0, 200))
# item_simulator.create_item(item)
item_simulator.create_many_items(5, (0, 200))
