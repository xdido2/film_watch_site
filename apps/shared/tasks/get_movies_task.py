import os
import time

import requests
from celery import shared_task
from dotenv import load_dotenv

from apps.movies.models.movie import Movie, ReleaseYear

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


@shared_task
def get_movies_from_api():
    try:
        content_videocdn = requests.get(f'{base_url_videocdn}?api_token={token_videocdn}&page={page}').json()

        last_page = content_videocdn['last_page']

        retry_attempts = 3
        retry_delay = 1
        for i in range(1, last_page):
            content_videocdn = requests.get(f'{base_url_videocdn}?api_token={token_videocdn}&page={i}').json()
            for j in range(0, content_videocdn['per_page']):
                result_videocdn = content_videocdn['data'][j]
                ru_title = result_videocdn['ru_title']
                url_tmdb_movie = f'{search_url_tmdb}&query={ru_title}'

                for attempt in range(retry_attempts):
                    try:
                        response = requests.get(url_tmdb_movie, headers=headers).json()
                        break
                    except requests.exceptions.ConnectionError as err:
                        if attempt < retry_attempts - 1:
                            time.sleep(retry_delay)
                        else:
                            raise err

                results_tmdb = response.get('results', [])
                if len(results_tmdb) == 0:
                    continue

                for k in results_tmdb:
                    url_tmdb_movie_detail = f"https://api.themoviedb.org/3/movie/{k.get('id')}?language=ru-RU"
                    result_tmdb = k
                    for attempt in range(retry_attempts):
                        try:
                            result_tmdb_movie_detail = requests.get(url_tmdb_movie_detail, headers=headers).json()
                            break  # If the request succeeds, exit the retry loop
                        except requests.exceptions.ConnectionError as err:
                            if attempt < retry_attempts - 1:
                                time.sleep(retry_delay)
                            else:
                                raise err

                    if result_tmdb_movie_detail.get('imdb_id') == result_videocdn['imdb_id'] or \
                            result_tmdb_movie_detail['original_title'] == result_videocdn['orig_title']:

                        existing_movie = Movie.objects.filter(orig_title=result_videocdn['orig_title'],
                                                              ru_title=ru_title).first()
                        if existing_movie:
                            continue

                        country = result_tmdb_movie_detail.get('production_countries', [])
                        country_name = country[0]['name'] if country else ''

                        # Handle the case when release_date is not available
                        release_year_str = result_tmdb.get('release_date', '')[:4]
                        if not release_year_str.isdigit():
                            release_year_obj = None
                        else:
                            release_year = int(release_year_str)
                            existing_year = ReleaseYear.objects.filter(year=release_year).first()
                            if existing_year:
                                release_year_obj = existing_year
                            else:
                                release_year_obj = ReleaseYear.objects.create(year=release_year)

                        movie = Movie(
                            id=result_tmdb.get('id'),
                            background_poster=result_tmdb.get('backdrop_path', ''),
                            poster=result_tmdb.get('poster_path', ''),
                            ru_title=ru_title,
                            orig_title=result_videocdn['orig_title'],
                            description=result_tmdb.get('overview', ''),
                            runtime=result_tmdb_movie_detail.get('runtime', 0),
                            vote=round(result_tmdb.get('vote_average', 0), 1),
                            vote_count=result_tmdb.get('vote_count', 0),
                            release_year=release_year_obj,
                            iframe_src=result_videocdn['iframe_src'],
                            translate=result_videocdn['translations'][0].get('title', ''),
                            max_quality=result_videocdn['media'][0].get('max_quality'),
                            imdb_id=result_videocdn['imdb_id'],
                            kinopoisk_id=result_videocdn['kinopoisk_id'],
                            country=country_name,
                        )
                        movie.save()

                        for genre_id in result_tmdb.get('genre_ids', []):
                            movie.genre.add(genre_id)
                        movie.save()

                    else:
                        continue

                time.sleep(5)
    except Exception as err:
        print(err)
