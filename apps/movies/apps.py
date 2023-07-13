from django.apps import AppConfig


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.movies'

    # def ready(self):
    #     from root.task import get_genres_from_api, get_movies_from_api
    #     get_genres_from_api.delay()
    #     get_movies_from_api.delay()
