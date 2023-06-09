from django.urls import path

from movies.views.film import film_list_view, film_detail_view

urlpatterns = [
    path('', film_list_view, name='film-list'),

    path('details/<slug:slug>', film_detail_view, name='film-detail'),
]
