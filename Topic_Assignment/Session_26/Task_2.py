# Build a small Python script that fetches the latest price of Bitcoin and Ethereum from the 
# CoinGecko API and displays them with the current date and time.

import requests
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd,inr"
}
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        btc_usd = data.get("bitcoin", {}).get("usd", 0)
        btc_inr = data.get("bitcoin", {}).get("inr", 0)
        eth_usd = data.get("ethereum", {}).get("usd", 0)
        eth_inr = data.get("ethereum", {}).get("inr", 0)
        
        print(f"=== Crypto Prices as of {now} ===")
        print(f"Bitcoin  (BTC) : ${btc_usd:,.2f} USD | ₹{btc_inr:,.2f} INR")
        print(f"Ethereum (ETH) : ${eth_usd:,.2f} USD | ₹{eth_inr:,.2f} INR")
    else:
        print(f"Failed to fetch price from CoinGecko. Status: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
