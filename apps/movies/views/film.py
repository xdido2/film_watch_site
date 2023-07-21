from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.movies.forms.comment import CommentForm
from apps.movies.models.comment import Comment
from apps.movies.models.history import History
from apps.movies.models.movie import Movie, Genre, ReleaseYear
from apps.movies.filters.release_years import CombinedReleaseYearFilter


def film_list_view(request):
    movies = Movie.objects.all()
    release_year_filter = CombinedReleaseYearFilter(request.GET.dict(), queryset=movies)
    last_comments = Comment.objects.all()[:2]
    release_years = ReleaseYear.objects.all()
    genres = Genre.objects.all()
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    p = Paginator(release_year_filter.qs, 15)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'slider_movies': slider_movies,
        'last_comments': last_comments,
        'release_years': release_years,
        'genres': genres,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)


def film_detail_view(request, slug):
    movie = get_object_or_404(Movie, slug_link=slug)
    genres = Genre.objects.all()
    last_comments = Comment.objects.all()[:2]
    comments = Comment.objects.filter(movie=movie)
    suggest_movies = Movie.objects.filter(vote__gt=6.0, poster__isnull=False)[:4]
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

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(movie=movie, user=user, content=form.data.get('content'))
            return HttpResponseRedirect(movie.get_absolute_url())
        else:
            ValidationError('User must be register!')

    context = {
        'movie': movie,
        'last_comments': last_comments,
        'suggest': suggest_movies,
        'comments': comments,
        'genres': genres,
        'is_favourite': is_favourite,
    }
    return render(request, 'films/main_content/movie-detail.html', context)
