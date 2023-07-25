from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from apps.movies.models.comment import Comment
from apps.movies.models.movie import Movie, ReleaseYear, Genre
from apps.site_info.models.about import Settings


def search_view(request):
    query = request.GET.get('q')
    genres = Genre.objects.all()
    site_info = Settings.objects.first()
    last_comments = Comment.objects.all()[:2]
    release_years = ReleaseYear.objects.all()
    slider_movies = Movie.objects.filter(vote__gt=1.0, background_poster__isnull=False).order_by('-vote_count')[:5]

    data = []
    if query == '':
        return redirect('film-list')
    else:
        from movies.documents import MoviesIndex

        s = MoviesIndex.search().query("multi_match", query=query, fields=["*"])

        for hit in s:
            data.append(hit)

        p = Paginator(data, 18)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)

        context = {
            'total_count_movie': len(data),
            'slider_movies': slider_movies,
            'release_years': release_years,
            'site_info': site_info,
            'genres': genres,
            'last_comments': last_comments,
            'page_obj': page_obj,
        }
        return render(request, 'films/main_content/search.html', context)
