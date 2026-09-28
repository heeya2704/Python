# Save the fetched data (name, current price, price change %, 24h high, 24h low) for the top 10 
# cryptocurrencies into a CSV file named crypto_prices.csv using the csv module.

import requests
import csv
import os

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    coins = response.json()
    file_path = os.path.join(os.path.dirname(__file__), "crypto_prices.csv")
    
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Current Price (USD)", "24h Price Change (%)", "24h High (USD)", "24h Low (USD)"])
        
        for coin in coins:
            writer.writerow([
                coin.get("name"),
                coin.get("current_price"),
                coin.get("price_change_percentage_24h"),
                coin.get("high_24h"),
                coin.get("low_24h")
            ])
            
    print(f"Data for top 10 cryptocurrencies successfully written to: '{file_path}'")
else:
    print(f"Failed to fetch data from API. Status Code: {response.status_code}")
