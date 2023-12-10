from pytube import YouTube
from googleapiclient.discovery import build
import os


def audio_downloader(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # You can customize the file name and format
    audio_file_path = "downloaded_audio.mp3"

    # Download the audio content to a file
    audio_stream.download(output_path=os.path.dirname(
        audio_file_path), filename=os.path.basename(audio_file_path))

    return audio_file_path
