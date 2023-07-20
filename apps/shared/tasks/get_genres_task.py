import os
import time

import requests
from celery import shared_task
from dotenv import load_dotenv

load_dotenv()

base_url_videocdn = 'https://videocdn.tv/api/movies'
search_url_tmdb = 'https://api.themoviedb.org/3/search/movie?include_adult=false&language=ru-RU&page=1'
token_videocdn = os.getenv('API_TOKEN_VIDEOCDN')
token_tmdb = os.getenv('API_TOKEN_TMDB')
page_limit = 100
page = 1

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token_tmdb}"
}

retry_attempts = 3
retry_delay = 1
batch_size = 10


@shared_task
def get_genres_from_api():
    from apps.movies.models.movie import Genre

    url = "https://api.themoviedb.org/3/genre/movie/list?language=ru"
    response = requests.get(url, headers=headers).json()
    genres = response.get('genres', [])
    existing_genres = Genre.objects.filter(name__in=[genre['name'] for genre in genres])
    existing_genre_names = set(genre.name for genre in existing_genres)
    new_genres = [
        Genre(id=genre['id'], name=genre['name'])
        for genre in genres
        if genre['name'] not in existing_genre_names
    ]
    Genre.objects.bulk_create(new_genres)