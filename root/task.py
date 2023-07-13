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


@shared_task
def get_movies_from_api():
    from apps.movies.models.movie import Movie

    content_videocdn = requests.get(f'{base_url_videocdn}?api_token={token_videocdn}&page={page}').json()
    last_page = content_videocdn['last_page']

    for i in range(1, last_page + 1):
        content_videocdn = requests.get(f'{base_url_videocdn}?api_token={token_videocdn}&page={i}').json()
        movies = content_videocdn['data']
        movie_objects = []

        for j in range(0, len(movies), batch_size):
            batch = movies[j:j + batch_size]
            orig_titles = [movie['orig_title'] for movie in batch]
            url_tmdb_movie = f'{search_url_tmdb}&query={"|".join(orig_titles)}'
            try:
                response = requests.get(url_tmdb_movie, headers=headers).json()
            except requests.exceptions.ConnectionError as err:
                raise err
            results_tmdb = response.get('results', [])
            for k, result_videocdn in enumerate(batch):
                if len(results_tmdb) <= k:
                    continue
                result_tmdb = results_tmdb[k]
                url_tmdb_movie_detail = f"https://api.themoviedb.org/3/movie/{result_tmdb.get('id')}?language=ru-RU"
                try:
                    result_tmdb_movie_detail = requests.get(url_tmdb_movie_detail, headers=headers).json()
                except requests.exceptions.ConnectionError as err:
                    raise err
                existing_movie = Movie.objects.filter(ru_title=result_videocdn['ru_title'],
                                                      orig_title=result_videocdn['orig_title']).first()
                if existing_movie:
                    continue
                country = result_tmdb_movie_detail.get('production_countries', [])
                country_name = country[0]['name'] if country else ''
                movie = Movie(
                    id=result_tmdb.get('id'),
                    background_poster=result_tmdb.get('backdrop_path', ''),
                    poster=result_tmdb.get('poster_path', ''),
                    ru_title=result_videocdn['ru_title'],
                    orig_title=result_videocdn['orig_title'],
                    description=result_tmdb.get('overview', ''),
                    runtime=result_tmdb_movie_detail.get('runtime', 0),
                    vote=round(result_tmdb.get('vote_average', 0), 1),
                    vote_count=result_tmdb.get('vote_count', 0),
                    release_date=result_tmdb.get('release_date', ''),
                    iframe_src=result_videocdn['iframe_src'],
                    translate=result_videocdn['translations'][0].get('title', ''),
                    max_quality=result_videocdn['media'][0].get('max_quality'),
                    imdb_id=result_videocdn['imdb_id'],
                    kinopoisk_id=result_videocdn['kinopoisk_id'],
                    country=country_name,
                )
                movie_objects.append(movie)

            time.sleep(5)

        if movie_objects:
            Movie.objects.bulk_create(movie_objects)
