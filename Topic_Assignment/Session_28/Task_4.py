# Build a function rank_coins_by_volume(data) that sorts all coins by their total traded volume 
# in descending order and prints the top 5 coins with their rank and volume.

import json
import os

def rank_coins_by_volume(data):
    if not data:
        print("No data to rank.")
        return
    
    sorted_coins = sorted(data, key=lambda coin: float(coin.get("quoteVolume", 0)), reverse=True)
    
    print("=== Top 5 Coins by Traded Volume (24h USDT) ===")
    print(f"{'Rank':<6} {'Symbol':<12} {'Volume (USDT)':<20}")
    print("-" * 40)
    for rank, coin in enumerate(sorted_coins[:5], start=1):
        symbol = coin.get("symbol")
        volume = float(coin.get("quoteVolume", 0))
        print(f"{rank:<6} {symbol:<12} ${volume:<19,.2f}")

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "crypto_data.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        rank_coins_by_volume(data)
    else:
        print(f"File '{file_path}' not found. Please run Task_1.py first.")
