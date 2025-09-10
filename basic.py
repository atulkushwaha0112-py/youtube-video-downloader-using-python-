# Code By Atul Kushwaha

from pytubefix import YouTube
from pytubefix.cli import on_progress

# Hardcoded URL example
url = "Youtube Url"

if '?' in url:
    url = url.split('?')[0]

yt = YouTube(url, on_progress_callback=on_progress)

# Print video details
print(f"Title   : {yt.title}")
print(f"Author  : {yt.author}")
print(f"Length  : {yt.length // 60} minutes {yt.length % 60} seconds")


stream = yt.streams.get_highest_resolution()
print(f"Downloading in: {stream.resolution}")

# Download the video
stream.download()
print("\n Download complete!")
