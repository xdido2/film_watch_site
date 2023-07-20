from django.apps import AppConfig

# from apps.shared.tasks.get_genres_task import get_genres_from_api
# from apps.shared.tasks.get_movies_task import get_movies_from_api

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.movies'

    # def ready(self):
    #     get_genres_from_api.delay()
    #     get_movies_from_api()
