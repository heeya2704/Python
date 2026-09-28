# Combine data from two APIs: fetch the current temperature in Mumbai from OpenWeatherMap and 
# the latest Bitcoin price from CoinGecko, then display both results together in a single output.
# 
# Constraint: Handle errors gracefully if either API call fails and show an appropriate message.

import requests

def fetch_mumbai_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return f"{data['current_weather']['temperature']}°C"
        return "Weather Data Unavailable (HTTP Error)"
    except Exception as e:
        return f"Weather Error: {e}"

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            data = res.json()
            price = data.get("bitcoin", {}).get("usd")
            return f"${price:,.2f} USD"
        return "Bitcoin Price Unavailable (HTTP Error)"
    except Exception as e:
        return f"Bitcoin Error: {e}"

def display_dashboard():
    print("==========================================")
    print("      MUMBAI & CRYPTO DASHBOARD           ")
    print("==========================================")
    
    weather = fetch_mumbai_weather()
    print(f"Mumbai Temperature : {weather}")
    
    btc_price = fetch_bitcoin_price()
    print(f"Bitcoin Price (USD): {btc_price}")
    print("==========================================")

if __name__ == "__main__":
    display_dashboard()
