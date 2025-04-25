import os
import sqlite3
import pandas as pd

CLEAN_FOLDER = 'youtube_clean_data'
DB_FILE = 'youtube.db'

# Connect to SQLite database (creates it if not exists)
conn = sqlite3.connect(DB_FILE)

for filename in os.listdir(CLEAN_FOLDER):
    if filename.endswith('.csv'):
        filepath = os.path.join(CLEAN_FOLDER, filename)
        df = pd.read_csv(filepath)

        # Use one table for all video data (append mode)
        df.to_sql('youtube_videos', conn, if_exists='append', index=False)
        print(f"[✓] Loaded: {filename} → youtube_videos table")

conn.close()
