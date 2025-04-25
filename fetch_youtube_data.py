import requests
import json
from datetime import datetime
import os

# Replace these with your own values
API_KEY = 'AIzaSyAvp1pFGU0I8hZ_85dbmvv-XUIPknhnKds'
CHANNEL_ID = 'UCChmJrVa8kDg05JfCmxpLRw'

# Folder to store data
RAW_DATA_DIR = 'youtube_raw_data'
os.makedirs(RAW_DATA_DIR, exist_ok=True)


def fetch_youtube_data():
    url = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?key={API_KEY}&channelId={CHANNEL_ID}"
        f"&part=snippet,id&order=date&maxResults=20"
    )
    response = requests.get(url)
    data = response.json()

    from datetime import datetime, timezone
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')

    filename = f"{RAW_DATA_DIR}/youtube_data_{timestamp}.json"

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"[✓] Data saved to {filename}")


if __name__ == "__main__":
    fetch_youtube_data()
