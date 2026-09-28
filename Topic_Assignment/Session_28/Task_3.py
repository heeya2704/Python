# Create a script that calculates the average price of all coins in your crypto_data.json, 
# then prints a list of all coins currently trading below this average price.

import json
import os

def analyze_below_average_prices():
    file_path = os.path.join(os.path.dirname(__file__), "crypto_data.json")
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Please run Task_1.py first.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    prices = [float(coin.get("lastPrice", 0)) for coin in data]
    if not prices:
        print("No price data found.")
        return

    avg_price = sum(prices) / len(prices)
    print(f"Average Price of all coins in dataset: ${avg_price:,.2f}\n")
    
    print(f"{'Symbol':<12} {'Current Price ($)':<18}")
    print("-" * 30)
    for coin in data:
        price = float(coin.get("lastPrice", 0))
        if price < avg_price:
            print(f"{coin.get('symbol'):<12} ${price:<17,.2f}")

if __name__ == "__main__":
    analyze_below_average_prices()
