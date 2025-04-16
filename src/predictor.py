import json
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib


def prepare_training_data():
    with open("data/filtered_items.json", "r") as f:
        data = json.load(f)

    X, y = [], []
    for item_id, item in data.items():
        x_row = [item["high"], item["low"]]
        target = (item["high"] + item["low"]) / 2
        X.append(x_row)
        y.append(target)

    return np.array(X), np.array(y)


def train_model():
    X, y = prepare_training_data()
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, "models/flipping_model.pkl")
    print("[✓] Model trained and saved.")
