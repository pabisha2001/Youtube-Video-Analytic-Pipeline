import os
import json
import pandas as pd
from datetime import datetime

RAW_FOLDER = 'youtube_raw_data'
CLEAN_FOLDER = 'youtube_clean_data'
os.makedirs(CLEAN_FOLDER, exist_ok=True)


def load_and_clean(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    cleaned_rows = []

    for item in data.get('items', []):
        video_id = item.get('id', {}).get('videoId')
        snippet = item.get('snippet', {})
        if not snippet:
            continue

        cleaned_rows.append({
            'video_id': video_id,
            'title': snippet.get('title'),
            'description': snippet.get('description'),
            'published_at': snippet.get('publishedAt'),
            'channel_title': snippet.get('channelTitle'),
            'thumbnail_url': snippet.get('thumbnails', {}).get('default', {}).get('url')
        })

    return pd.DataFrame(cleaned_rows)


# Clean all JSON files in the raw data folder
for filename in os.listdir(RAW_FOLDER):
    if filename.endswith('.json'):
        filepath = os.path.join(RAW_FOLDER, filename)
        df = load_and_clean(filepath)

        # Save cleaned file
        timestamp = filename.replace("youtube_data_", "").replace(".json", "")
        output_path = os.path.join(CLEAN_FOLDER, f"cleaned_data_{timestamp}.csv")
        df.to_csv(output_path, index=False)
        print(f"[✓] Cleaned file saved: {output_path}")
