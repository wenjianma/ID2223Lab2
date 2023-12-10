from pytube import YouTube
from googleapiclient.discovery import build

# set your own api_key
# https://console.developers.google.com/
# and also
# earch for "YouTube Data API v3" in the search bar
# to enable the YouTube Data API v3
api_key = "AIzaSyDeEo3FVj4Te3b86n16zNlyBZcbd3WUsF0"
youtube = build("youtube", "v3", developerKey=api_key)

# set the taget video url
video_url = "https://www.youtube.com/watch?v=EvE5cYNXufY"
video_id = video_url.split("v=")[1]

video_details = youtube.videos().list(
    part="snippet,contentDetails", id=video_id).execute()

audio_url = video_details["items"][0]["id"]

yt = YouTube(video_url)
audio_stream = yt.streams.filter(only_audio=True).first()
# set the save path
audio_stream.download(
    output_path="D:\Workspace\ID2223\ID2223Lab2", filename="danchaofan.mp3")
