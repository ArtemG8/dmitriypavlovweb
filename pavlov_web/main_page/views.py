import os
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from dotenv import load_dotenv
import requests


def main(request):
    load_dotenv()
    # Получение информации о канале
    channel_url = f'https://www.googleapis.com/youtube/v3/channels?part=contentDetails,statistics&id={os.getenv("CHANNEL_ID")}&key={os.getenv("API_KEY")}'
    channel_response = requests.get(channel_url)
    channel_data = channel_response.json()

    # Проверка на наличие данных о канале
    if 'items' in channel_data and len(channel_data['items']) > 0:
        statistics = channel_data['items'][0]['statistics']
        uploads_playlist_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    else:
        statistics = {}
        uploads_playlist_id = None

    # Получение видео из плейлиста загрузок
    videos = []
    if uploads_playlist_id:
        videos_url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_playlist_id}&maxResults=3&key={os.getenv("API_KEY")}'
        videos_response = requests.get(videos_url)
        videos_data = videos_response.json()

        # Проверка на наличие видео
        if 'items' in videos_data:
            videos = [item['snippet'] for item in videos_data['items']]

    return render(request, 'main_page/index.html', {'statistics': statistics, 'videos': videos})
