from src.fetch_data import fetch_latest_prices, save_prices
from src.filter_items import filter_items
from src.predictor import train_model
from src.flip_logic import recommend_flips

if __name__ == "__main__":
    print("[1/4] Fetching prices...")
    data = fetch_latest_prices()
    save_prices(data)

    print("[2/4] Filtering items...")
    filter_items()

    print("[3/4] Training model...")
    train_model()

    print("[4/4] Recommending flips:")
    for item_id, profit in recommend_flips():
        print(f"Item {item_id} → Estimated profit: {profit} gp")
