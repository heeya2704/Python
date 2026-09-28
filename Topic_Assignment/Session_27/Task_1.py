# Use the requests library to fetch the top 10 cryptocurrencies and their current prices in USD 
# from the CoinGecko API (https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1). 
# Print the name and price of each coin.

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
    print("=== Top 10 Cryptocurrencies by Market Cap ===")
    for index, coin in enumerate(coins, start=1):
        name = coin.get("name")
        symbol = coin.get("symbol").upper()
        price = coin.get("current_price", 0)
        print(f"{index:2d}. {name} ({symbol}): ${price:,.2f}")
else:
    print(f"Failed to fetch data from CoinGecko. Status code: {response.status_code}")
