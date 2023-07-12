import os
import time
import requests
from celery import shared_task
from dotenv import load_dotenv

load_dotenv()

base_url_videocdn = 'https://videocdn.tv/api/movies'
base_url_tmdb = 'https://api.themoviedb.org/3/search/movie?include_adult=false&language=ru-RU&page=1'
token_videocdn = os.getenv('API_TOKEN_VIDEOCDN')
token_tmdb = os.getenv('API_TOKEN_TMDB')
page_limit = 100
page = 1

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token_tmdb}"
}

content_videocdn = requests.get(f'{base_url_videocdn}?api_token={token_videocdn}&page={page}').json()

last_page = content_videocdn['last_page']

retry_attempts = 3
retry_delay = 1

@shared_task
def get_genres_from_api():
    from apps.movies.models.movie import Genre

    url = "https://api.themoviedb.org/3/genre/movie/list?language=ru"
    response = requests.get(url, headers=headers).json()
    for result in response.get('genres', []):
        existing_genre = Genre.objects.filter(name=result['name']).first()
        if existing_genre:
            continue
        genre = Genre(
            id=result['id'],
            name=result['name'],
        )
        genre.save()

@shared_task
def get_movies_from_api():
    from apps.movies.models.movie import Movie

    for i in range(last_page):
        content_videocdn = requests.get(f'{base_url_videocdn}?api_token={token_videocdn}&page={i}').json()
        for j in range(0, content_videocdn['per_page']):
            result_videocdn = content_videocdn['data'][j]
            orig_title = result_videocdn['orig_title']
            url_tmdb = f'{base_url_tmdb}&query={orig_title}'

            for attempt in range(retry_attempts):
                try:
                    response = requests.get(url_tmdb, headers=headers).json()
                    break  # If the request succeeds, exit the retry loop
                except requests.exceptions.ConnectionError as err:
                    if attempt < retry_attempts - 1:
                        time.sleep(retry_delay)
                    else:
                        raise err

            results_tmdb = response.get('results', [])
            if len(results_tmdb) == 0:
                continue

            result_tmdb = results_tmdb[0]
            existing_movie = Movie.objects.filter(ru_title=result_videocdn['ru_title'], orig_title=orig_title).first()
            if existing_movie:
                continue

            movie = Movie(
                background_poster=result_tmdb.get('backdrop_path', ''),
                poster=result_tmdb.get('poster_path', ''),
                ru_title=result_videocdn['ru_title'],
                orig_title=orig_title,
                description=result_tmdb.get('overview', ''),
                vote=round(result_tmdb.get('vote_average', 0), 1),
                vote_count=result_tmdb.get('vote_count', 0),
                release_date=result_tmdb.get('release_date', ''),
                iframe_src=result_videocdn['iframe_src'],
                imdb_id=result_videocdn['imdb_id'],
                kinopoisk_id=result_videocdn['kinopoisk_id'],
            )
            movie.save()

            for genre_id in result_tmdb.get('genre_ids', []):
                movie.genre.add(genre_id)
            movie.save()

        time.sleep(5)
