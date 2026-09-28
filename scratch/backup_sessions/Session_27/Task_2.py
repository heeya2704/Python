# Extend your script to also fetch and display the 24-hour price change percentage, 
# 24-hour high, and 24-hour low for each of the top 10 cryptocurrencies.

import requests

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
    print(f"{'Rank':<5} {'Name':<20} {'Price ($)':<12} {'24h Change (%)':<15} {'24h High ($)':<14} {'24h Low ($)':<14}")
    print("-" * 80)
    
    for rank, coin in enumerate(coins, start=1):
        name = coin.get("name")
        price = coin.get("current_price", 0)
        change_24h = coin.get("price_change_percentage_24h", 0)
        high_24h = coin.get("high_24h", 0)
        low_24h = coin.get("low_24h", 0)
        
        print(f"{rank:<5} {name:<20} ${price:<11,.2f} {change_24h:<+14.2f}% ${high_24h:<13,.2f} ${low_24h:<13,.2f}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
