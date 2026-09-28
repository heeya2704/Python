# Write a Python function find_most_volatile_coin(data) that takes the loaded Binance coin 
# data and returns the symbol of the coin with the highest percentage price change in the last 24 hours.

import json
import os

def find_most_volatile_coin(data):
    if not data:
        return None, 0.0
    
    most_volatile = max(data, key=lambda coin: abs(float(coin.get("priceChangePercent", 0))))
    return most_volatile.get("symbol"), float(most_volatile.get("priceChangePercent", 0))

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "crypto_data.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            coin_data = json.load(f)
            
        symbol, change_pct = find_most_volatile_coin(coin_data)
        print(f"Most Volatile Coin: {symbol} with 24h Price Change: {change_pct:+.2f}%")
    else:
        print(f"File '{file_path}' not found. Please run Task_1.py first to generate JSON data.")
