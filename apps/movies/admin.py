from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.movies.models.comment import Comment
from apps.movies.models.movie import Movie, Genre

admin.site.site_header = 'DIDO CINEMA administration'
admin.site.title = 'DIDO CINEMA administration'
admin.site.index_title = 'Welcome to DIDO CINEMA administration'


@admin.register(Movie)
class MovieModalAdmin(ModelAdmin):
    list_filter = ('release_year__year',)
    search_fields = ('ru_title', 'orig_title', 'description',)


admin.site.register(Genre)


@admin.register(Comment)
class CommentModelAdmin(ModelAdmin):
    list_display = ('content', 'is_approved', 'created_at',)
    list_filter = ('is_approved',)
