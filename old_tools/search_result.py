from googleapiclient.discovery import build


def get_first_video_url(api_key, query):
    youtube = build("youtube", "v3", developerKey=api_key)

    # Call the search.list method to search for videos
    search_response = youtube.search().list(
        q=query,
        part="id",
        type="video",
        maxResults=1
    ).execute()

    # Get the video ID of the first result
    if "items" in search_response and search_response["items"]:
        video_id = search_response["items"][0]["id"]["videoId"]

        # Construct the video URL
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        return video_url
    else:
        return None


# set your own api_key
api_key = "AIzaSyDeEo3FVj4Te3b86n16zNlyBZcbd3WUsF0"
search_query = "台湾"

# Get the first video URL
result = get_first_video_url(api_key, search_query)

if result:
    print(f"The URL of the first video in the search results: {result}")
else:
    print("No video found in the search results.")
