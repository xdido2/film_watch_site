from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render

from apps.movies.models.comment import Comment
from apps.movies.models.movie import Movie, ReleaseYear, Genre


def release_years_list_view(request, year):
    release_years = ReleaseYear.objects.all()
    release_years_movie = Movie.objects.filter(release_year__year=year)
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    last_comments = Comment.objects.all()[:2]
    genres = Genre.objects.all()
    p = Paginator(release_years_movie, 15)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'last_comments': last_comments,
        'slider_movies': slider_movies,
        'release_years': release_years,
        'genres': genres,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)
