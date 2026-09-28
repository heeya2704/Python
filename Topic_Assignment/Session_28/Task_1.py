# Fetch the latest 24-hour price and volume data for at least 10 popular cryptocurrencies 
# using the Binance API and save the raw JSON response to a file named crypto_data.json.

import requests
import json
import os

url = "https://api.binance.com/api/v3/ticker/24hr"

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        all_tickers = response.json()
        
        popular_symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "ADAUSDT", 
                           "XRPUSDT", "DOGEUSDT", "DOTUSDT", "AVAXUSDT", "LINKUSDT"]
        
        filtered_data = [ticker for ticker in all_tickers if ticker.get("symbol") in popular_symbols]
        
        file_path = os.path.join(os.path.dirname(__file__), "crypto_data.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(filtered_data, f, indent=4)
            
        print(f"Successfully saved {len(filtered_data)} coins data to '{file_path}'")
    else:
        print(f"Failed to fetch Binance data. Status Code: {response.status_code}")
except Exception as e:
    print(f"Error fetching Binance API data: {e}")
