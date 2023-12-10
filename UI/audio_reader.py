from googleapiclient.discovery import build
import requests
import json
from pydub import AudioSegment


api_key = "AIzaSyDeEo3FVj4Te3b86n16zNlyBZcbd3WUsF0"
youtube = build("youtube", "v3", developerKey=api_key)

API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

ASR_API_URL = "https://api-inference.huggingface.co/models/Wenjian12581/whisper-small-mandarin"


def get_videos_info(api_key, query):
    youtube = build("youtube", "v3", developerKey=api_key)

    # Call the search.list method to search for videos
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        maxResults=5
    ).execute()

    videos_info = []

    # Loop through the results and extract information
    for item in search_response.get("items", []):
        video_id = item.get("id", {}).get("videoId")
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_name = item.get("snippet", {}).get("title")

        # Fetch detailed information for each video
        video_details = youtube.videos().list(
            part="contentDetails",
            id=video_id
        ).execute()

        # Handle missing contentDetails or duration
        content_details = video_details["items"][0].get("contentDetails", {})
        video_duration = content_details.get("duration", "N/A")

        video_info = {
            "name": video_name,
            "duration": video_duration,
            "url": video_url
        }

        videos_info.append(video_info)

    return videos_info


def transcribe_audio(audio_data):
    if isinstance(audio_data, tuple) and len(audio_data) == 2:
        audio_array = audio_data[1]

        # Ensure that audio_array has at least one dimension
        if audio_array.ndim > 0:
            frame_rate = audio_array.shape[0] // (
                len(audio_array) // audio_data[0])

            # Convert to WAV format
            audio_segment = AudioSegment(
                audio_array.tobytes(),
                frame_rate=frame_rate,
                sample_width=audio_array.dtype.itemsize,
                channels=1
            )
            audio_bytes = audio_segment.export(format="wav").read()

            # Use the correct Hugging Face API URL for ASR
            response = requests.post(
                ASR_API_URL, headers=headers, data=audio_bytes
            )

            # Print additional debugging information
            print("Request Headers:", headers)
            print("API Response Status Code:", response.status_code)

            if response.status_code == 200:
                result = json.loads(response.content.decode("utf-8"))
                # print(result.get("text", "No transcription result"))
                api_key = "AIzaSyDeEo3FVj4Te3b86n16zNlyBZcbd3WUsF0"
                search_query = result.get("text", "No transcription result")
                result = get_videos_info(api_key, search_query)
                return result
            else:
                return f"Error: {response.status_code}, {response.content.decode('utf-8')}"
        else:
            return f"Invalid audio data format: audio_array has {audio_array.ndim} dimensions"
    else:
        return "Invalid audio data format: not a tuple or does not have 2 elements"
