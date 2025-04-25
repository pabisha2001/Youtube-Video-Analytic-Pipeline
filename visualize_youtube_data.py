import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to database
conn = sqlite3.connect('youtube.db')

# Load data from the youtube_videos table
df = pd.read_sql("SELECT * FROM youtube_videos", conn)

# Convert published_at to datetime
df['published_at'] = pd.to_datetime(df['published_at'])

# 1. 📅 Number of videos published per day
df['date'] = df['published_at'].dt.date
video_counts = df.groupby('date').size()

plt.figure(figsize=(10, 5))
video_counts.plot(kind='bar')
plt.title("Number of Videos Published Per Day")
plt.xlabel("Date")
plt.ylabel("Video Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. 📈 Top 10 Longest Titles
df['title_length'] = df['title'].apply(lambda x: len(str(x)))
top_titles = df[['title', 'title_length']].sort_values(by='title_length', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_titles, y='title', x='title_length', palette='magma')
plt.title("Top 10 Longest Video Titles")
plt.xlabel("Title Length")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()

# 3. 🎬 Video count by channel
channel_counts = df['channel_title'].value_counts().head(10)

plt.figure(figsize=(10, 5))
channel_counts.plot(kind='barh', color='skyblue')
plt.title("Top Channels by Number of Videos")
plt.xlabel("Number of Videos")
plt.ylabel("Channel")
plt.tight_layout()
plt.show()

conn.close()
