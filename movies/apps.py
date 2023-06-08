from django.apps import AppConfig


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'

    # def ready(self):
    #     from root.task import movie_data_form_api
    #     movie_data_form_api.delay()
