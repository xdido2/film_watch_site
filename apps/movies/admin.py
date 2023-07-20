from django.contrib import admin

from apps.movies.models.comment import Comment
from apps.movies.models.movie import Movie, Genre

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Comment)
