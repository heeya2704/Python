# Use the requests.Session() object to fetch your Flipkart order history page twice in a row 
# (without logging in), and print the response status codes for both requests.
# 
# Hint: Observe if cookies or session headers change between requests.

import requests

url = "https://www.flipkart.com/account/orders"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

with requests.Session() as session:
    session.headers.update(headers)
    
    print("--- Request 1 ---")
    response1 = session.get(url)
    print(f"Status Code 1: {response1.status_code}")
    print(f"Cookies after Request 1: {session.cookies.get_dict()}")
    
    print("\n--- Request 2 ---")
    response2 = session.get(url)
    print(f"Status Code 2: {response2.status_code}")
    print(f"Cookies after Request 2: {session.cookies.get_dict()}")
