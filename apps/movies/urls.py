from django.urls import path

from apps.movies.filters.new_films import new_films_list_view, popular_films_list_view, a_z_films_list_view, \
    z_a_films_list_view
from apps.movies.views.film import add_film_view
from apps.movies.views.film import film_list_view, film_detail_view
from apps.movies.views.genres import genre_list_view
from apps.movies.views.release_years import release_years_list_view
from apps.movies.views.search import search_view
from apps.movies.views.order import order_view
from apps.movies.views.comment import post_comment

urlpatterns = [
    path('', film_list_view, name='film-list'),
    path('details/<slug:slug>', film_detail_view, name='film-detail'),
    path('genre/<slug:slug>', genre_list_view, name='genre-list'),
    path('new/', new_films_list_view, name='new_films-list'),
    path('popular/', popular_films_list_view, name='popular_films-list'),
    path('sort_а_я/', a_z_films_list_view, name='sort_a_z_films-list'),
    path('sort_я_а/', z_a_films_list_view, name='sort_z_a_films-list'),
    path('release_year/<int:year>', release_years_list_view, name='release_year-list'),
    path('search/', search_view, name='search'),
    path('add-content/', add_film_view, name='content'),
    path('order-film/', order_view, name='film-order'),
    path('post-comment/<int:movie_id>', post_comment, name='post-comment'),
]
