import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ETHERSCAN_API_KEY")

address = "0xF977814e90dA44bFA03b6295A0616a897441aceC"

params = {
    "chainid": 1,
    "module": "nametag",
    "action": "getaddresstag",
    "address": address,
    "apikey": API_KEY,
}

response = requests.get(
    "https://api.etherscan.io/v2/api",
    params=params,
)

print(response.url)
print(response.json())
print("All done.")