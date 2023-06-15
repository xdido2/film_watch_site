from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from apps.movies.models.movie import Movie


def film_list_view(request):
    movies = Movie.objects.all()
    latest_movies = Movie.objects.order_by('-released')
    p = Paginator(movies, 18)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    context = {
        'total_count_movie': movies.count(),
        'latest_movies': latest_movies,
        'page_obj': page_obj,
    }
    return render(request, 'films/main_content/film-list.html', context)


def film_detail_view(request, slug):
    movie = get_object_or_404(Movie, slug_link=slug)
    context = {
        'movie': movie,
    }
    return render(request, 'films/main_content/film-detail.html', context)
