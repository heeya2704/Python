# Add error handling to your code so that if the API request fails or returns an error, 
# your script prints a user-friendly message instead of crashing.
# 
# Hint: Check the response status code and handle exceptions from the requests library.

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

def fetch_and_save_crypto():
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for 4xx or 5xx codes
        
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
                
        print(f"Successfully processed {len(coins)} cryptocurrencies and saved to '{file_path}'")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"[HTTP Error] Failed to fetch crypto data: {http_err}")
    except requests.exceptions.ConnectionError:
        print("[Network Error] Could not connect to CoinGecko server. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("[Timeout Error] The request to CoinGecko timed out. Please try again later.")
    except requests.exceptions.RequestException as req_err:
        print(f"[Request Error] An error occurred while handling the request: {req_err}")
    except Exception as err:
        print(f"[Unexpected Error] {err}")

if __name__ == "__main__":
    fetch_and_save_crypto()
