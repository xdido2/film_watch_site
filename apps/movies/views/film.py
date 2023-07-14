from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from apps.movies.models.movie import Movie
from apps.users.models.history import History


def film_list_view(request):
    movies = Movie.objects.all()
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]
    p = Paginator(movies, 15)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    context = {
        'total_count_movie': movies.count(),
        'slider_movies': slider_movies,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/movie-list.html', context)


def film_detail_view(request, slug):
    movie = get_object_or_404(Movie, slug_link=slug)
    suggest_movies = Movie.objects.filter(vote__gt=6.0, poster__isnull=False)[:4]
    movie_id = movie.id
    user = request.user
    if user.id:
        if not History.objects.filter(user_id=user.pk, movie_id=movie_id).exists():
            history = History.objects.create(user_id=user.pk, movie_id=movie_id)
            history.save()
        History.objects.filter(user_id=user.pk, movie_id=movie_id).delete()
        history = History.objects.create(user_id=user.pk, movie_id=movie_id)
        history.save()

    context = {
        'movie': movie,
        'suggest': suggest_movies,
    }
    return render(request, 'films/main_content/movie-detail.html', context)
