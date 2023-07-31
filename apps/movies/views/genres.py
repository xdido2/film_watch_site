from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render

from apps.movies.models.comment import Comment
from apps.movies.models.movie import Genre
from apps.movies.models.movie import Movie
from apps.movies.models.movie import ReleaseYear
from apps.shared.utils.sort_filter import movie_sort_filter
from apps.site_info.models.about import Settings


def genre_list_view(request, slug):
    release_years = ReleaseYear.objects.all()
    genres_movie = Movie.objects.filter(genre__slug_link=slug)
    site_info = Settings.objects.first()
    _filter = request.GET.get('sort')
    _year = request.GET.get('year')
    sort_filter = movie_sort_filter(_filter, genres_movie, _year)
    # release_year_filter = CombinedReleaseYearFilter(request.GET.dict(), queryset=genres_movie)
    last_comments = Comment.objects.all(is_approved=True)[:2]
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    genres = Genre.objects.all()
    p = Paginator(sort_filter[0], 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'last_comments': last_comments,
        'filter_name': sort_filter[1],
        'site_info': site_info,
        'current_year': _year,
        'slider_movies': slider_movies,
        'genres': genres,
        'release_years': release_years,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)
