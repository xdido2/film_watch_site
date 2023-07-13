from django.contrib import admin

from apps.movies.models.movie import Movie, Genre

admin.site.register(Movie)
admin.site.register(Genre)
