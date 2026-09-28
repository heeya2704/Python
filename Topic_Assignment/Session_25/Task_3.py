# Simulate an async data fetch from two different APIs (for example, fetch trending songs 
# from Spotify and trending movies from BookMyShow) using Python's asyncio and httpx library, 
# and print both results when done.
# 
# Hint: Use asyncio.gather() to run both requests concurrently.

import asyncio
import httpx

async def fetch_spotify_trending(client):
    print("[Spotify] Fetching trending music data...")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = await client.get(url)
    if response.status_code == 200:
        return {"source": "Spotify", "trending_song": "Blinding Lights by The Weeknd"}
    return {"source": "Spotify", "error": "Fetch failed"}

async def fetch_bookmyshow_trending(client):
    print("[BookMyShow] Fetching trending movies data...")
    url = "https://jsonplaceholder.typicode.com/posts/2"
    response = await client.get(url)
    if response.status_code == 200:
        return {"source": "BookMyShow", "trending_movie": "Avatar: Fire and Ash"}
    return {"source": "BookMyShow", "error": "Fetch failed"}

async def main():
    async with httpx.AsyncClient() as client:
        # Running both async API requests concurrently using asyncio.gather()
        results = await asyncio.gather(
            fetch_spotify_trending(client),
            fetch_bookmyshow_trending(client)
        )
        
    print("\n--- Concurrent Fetch Results ---")
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())
