from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render

from apps.movies.models.comment import Comment
from apps.movies.models.movie import Genre
from apps.movies.models.movie import Movie
from apps.movies.models.movie import ReleaseYear


def new_films_list_view(request):
    release_years = ReleaseYear.objects.all()
    genres_movie = Movie.objects.order_by('-release_year__year')
    last_comments = Comment.objects.filter(is_approved=True)[:2]
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    genres = Genre.objects.all()
    p = Paginator(genres_movie, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'last_comments': last_comments,
        'slider_movies': slider_movies,
        'genres': genres,
        'release_years': release_years,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)


def popular_films_list_view(request):
    release_years = ReleaseYear.objects.all()
    movies = Movie.objects.order_by('-vote_count')
    last_comments = Comment.objects.filter(is_approved=True)[:2]
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    genres = Genre.objects.all()
    p = Paginator(movies, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'last_comments': last_comments,
        'slider_movies': slider_movies,
        'genres': genres,
        'release_years': release_years,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)


def a_z_films_list_view(request):
    release_years = ReleaseYear.objects.all()
    movies = Movie.objects.order_by('ru_title')
    last_comments = Comment.objects.filter(is_approved=True)[:2]
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    genres = Genre.objects.all()
    p = Paginator(movies, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'last_comments': last_comments,
        'slider_movies': slider_movies,
        'genres': genres,
        'release_years': release_years,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)


def z_a_films_list_view(request):
    release_years = ReleaseYear.objects.all()
    movies = Movie.objects.order_by('-ru_title')
    last_comments = Comment.objects.filter(is_approved=True)[:2]
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    genres = Genre.objects.all()
    p = Paginator(movies, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'last_comments': last_comments,
        'slider_movies': slider_movies,
        'genres': genres,
        'release_years': release_years,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)
