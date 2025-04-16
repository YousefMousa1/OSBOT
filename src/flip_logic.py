import json
import joblib

GE_TAX = 0.01


def calculate_profit(buy_price, sell_price):
    taxed_sell_price = sell_price * (1 - GE_TAX)
    return taxed_sell_price - buy_price


def recommend_flips():
    model = joblib.load("models/flipping_model.pkl")
    with open("data/filtered_items.json", "r") as f:
        data = json.load(f)

    recommendations = []
    for item_id, item in data.items():
        features = [[item["high"], item["low"]]]
        predicted_price = model.predict(features)[0]
        profit = calculate_profit(item["low"], predicted_price)
        if profit > 1000:
            recommendations.append((item_id, round(profit)))

    recommendations.sort(key=lambda x: -x[1])
    return recommendations