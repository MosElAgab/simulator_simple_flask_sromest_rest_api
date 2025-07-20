import os
import requests
from dotenv import load_dotenv

from store_simulator import StoreSimulator

load_dotenv()

def login(username, password):
    login_data = {
        "username": username,
        "password": password
    }
    response = requests.post(f"{base_url}/login", json=login_data)
    if response.ok:
        print("logged in successfully")
    access_token = response.json().get("access_token")
    authorization_header = {"Authorization": f"Bearer {access_token}"}
    return authorization_header


base_url = "http://3.84.18.152:5007"
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
if not username or not password:
    raise ValueError("USERNAME or PASSWORD not set.")

authorization_header = login(username, password)
store_simulator = StoreSimulator(base_url, authorization_header)


store_simulator.create_many_stores(5)
stores = store_simulator.get_stores()
ids = store_simulator.get_store_ids(stores)
