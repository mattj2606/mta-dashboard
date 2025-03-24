import os
import requests
from datetime import datetime

# Create folders if they don't exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/static", exist_ok=True)

def fetch_static_gtfs():
    print("Fetching static GTFS schedule...")
    url = "https://transitfeeds.com/p/mta/79/latest/download"  # Static GTFS feed
    response = requests.get(url)

    if response.status_code == 200:
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"data/static/static_gtfs_{now}.zip"
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved static GTFS data to {filepath}")
    else:
        print(f"❌ Failed to download static GTFS data. Status: {response.status_code}")

if __name__ == "__main__":
    fetch_static_gtfs()