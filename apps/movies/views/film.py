from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from apps.movies.forms.comment import CommentForm
from apps.movies.models.comment import Comment
from apps.movies.models.history import History
from apps.movies.models.movie import Movie, Genre, ReleaseYear
from apps.shared.tasks.get_genres_task import get_genres_from_api
from apps.shared.tasks.get_movies_task import get_movies_from_api
from apps.shared.utils.sort_filter import movie_sort_filter
from apps.site_info.models.about import Settings


def film_list_view(request):
    movies = Movie.objects.all()
    site_info = Settings.objects.first()
    _filter = request.GET.get('sort')
    _year = request.GET.get('year')
    sort_filter = movie_sort_filter(_filter, movies, _year)
    last_comments = Comment.objects.all()[:2]
    release_years = ReleaseYear.objects.all()
    genres = Genre.objects.all()
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    p = Paginator(sort_filter[0], 15)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'slider_movies': slider_movies,
        'filter_name': sort_filter[1],
        'site_info': site_info,
        'current_year': _year,
        'last_comments': last_comments,
        'release_years': release_years,
        'genres': genres,
        'page_obj': page_obj,
        'page': page_number,
    }
    return render(request, 'films/main_content/movie-list.html', context)


def film_detail_view(request, slug):
    movie = get_object_or_404(Movie, slug_link=slug)
    site_info = Settings.objects.first()
    genres = Genre.objects.all()
    last_comments = Comment.objects.all()[:2]
    comments = Comment.objects.filter(movie=movie)
    suggest_movies = Movie.objects.filter(genre__name=movie.genre.first(), vote__gt=6.0, poster__isnull=False)[:4]
    is_favourite = False
    movie_id = movie.id
    user = request.user
    if user.id:
        if not History.objects.filter(user_id=user.pk, movie_id=movie_id).exists():
            history = History.objects.create(user_id=user.pk, movie_id=movie_id)
            history.save()
        History.objects.filter(user_id=user.pk, movie_id=movie_id).delete()
        history = History.objects.create(user_id=user.pk, movie_id=movie_id)
        history.save()
    if movie.favourite.filter(id=user.id):
        is_favourite = True

    context = {
        'movie': movie,
        'site_info': site_info,
        'last_comments': last_comments,
        'suggest': suggest_movies,
        'comments': comments,
        'genres': genres,
        'is_favourite': is_favourite,
    }
    return render(request, 'films/main_content/movie-detail.html', context)


def add_film_view(request):
    get_genres_from_api.delay()
    get_movies_from_api.delay()

    return redirect('admin:index')
