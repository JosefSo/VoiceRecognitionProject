import os
from pytube import YouTube

# Set the URL of the YouTube video
url = 'https://www.youtube.com/watch?v=1qdTwvk7LCw'

# Create a YouTube object
yt = YouTube(url)

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Set the desired duration of the audio file in seconds
duration = 120

# Get the audio stream with the specified duration
audio_data = audio_stream.download(output_path='downloadedFromYouTube', filename='audio2.wav', timeout=10)

