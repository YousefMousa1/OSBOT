import requests
import time
import json
import os

BASE_URL = "https://prices.runescape.wiki/api/v1/osrs"
HEADERS = {"User-Agent": "osrs-flipping-bot"}


def fetch_latest_prices():
    url = f"{BASE_URL}/latest"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        raise Exception("Failed to fetch prices")


def save_prices(data, filename="data/latest_prices.json"):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    prices = fetch_latest_prices()
    save_prices(prices)
    print("[✓] Latest prices saved.")
