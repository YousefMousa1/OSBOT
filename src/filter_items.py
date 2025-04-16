import json

def filter_items(input_file="data/latest_prices.json", min_volume=1000, min_price=100000, max_price=1e9):
    with open(input_file, "r") as f:
        data = json.load(f)

    filtered = {}
    for item_id, item in data.items():
        if item["high"] is None or item["low"] is None:
            continue
        if item["high"] > max_price or item["low"] < min_price:
            continue
        if item.get("highTime", 0) == 0:
            continue
        filtered[item_id] = item

    with open("data/filtered_items.json", "w") as f:
        json.dump(filtered, f, indent=4)
    print(f"[✓] Filtered {len(filtered)} items.")
