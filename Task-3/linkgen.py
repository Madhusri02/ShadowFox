from googleapiclient.discovery import build
from linkgen import search_youtube_videos 
from dotenv import load_dotenv
import os

API_KEY = os.getenv("API_KEY")  # Access the API key

def search_youtube_videos(query, max_results):
    # API_KEY = "AIzaSyBxrj0UGS5pUrDXP5YRRlGsLpLYHirhC6s"
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )

    response = request.execute()

    video_links = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_links.append(f'https://www.youtube.com/watch?v={video_id}')

    return video_links


# query = "factorial of a number"
 
# max_results = 5

# videos = search_youtube_videos(query, max_results)
# for video in videos:
#     print(video)