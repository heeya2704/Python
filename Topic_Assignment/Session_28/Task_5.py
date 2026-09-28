# Automate your data fetch and analysis by scheduling your script to run every hour using the 
# schedule Python library, and add error handling to gracefully manage Binance API rate limits.
# 
# Hint: Catch HTTP 429 errors and implement a retry with exponential backoff.

import requests
import json
import time
import schedule
import os

BINANCE_URL = "https://api.binance.com/api/v3/ticker/24hr"

def fetch_with_backoff(url, max_retries=3):
    backoff = 2  # Initial delay in seconds
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:  # Rate limit error
                print(f"[Rate Limit] HTTP 429 received. Backing off for {backoff}s (Attempt {attempt}/{max_retries})...")
                time.sleep(backoff)
                backoff *= 2
            else:
                print(f"[HTTP Error] Status code {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"[Request Exception] {e}. Retrying in {backoff}s...")
            time.sleep(backoff)
            backoff *= 2
    return None

def scheduled_job():
    print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting scheduled Binance crypto analysis job...")
    data = fetch_with_backoff(BINANCE_URL)
    if data:
        popular = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]
        filtered = [coin for coin in data if coin.get("symbol") in popular]
        
        file_path = os.path.join(os.path.dirname(__file__), "crypto_data.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(filtered, f, indent=4)
        print(f"Successfully updated '{file_path}' with {len(filtered)} coins.")
    else:
        print("Scheduled job failed to fetch data.")

if __name__ == "__main__":
    print("Scheduling job to run every hour. Executing one iteration now for demonstration...")
    scheduled_job()
    
    # Schedule job every 1 hour
    schedule.every(1).hours.do(scheduled_job)
    print("Scheduler initialized. Press Ctrl+C to exit standing schedule.")
