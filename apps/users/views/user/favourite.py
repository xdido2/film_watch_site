from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from apps.movies.models.movie import Movie
from apps.movies.models.comment import Comment
from apps.movies.models.movie import Genre, ReleaseYear


def favourite_list_view(request):
    user = request.user
    favourite_list = user.movie_set.all()
    p = Paginator(favourite_list, 10)
    last_comments = Comment.objects.filter(is_approved=True)[:2]
    release_years = ReleaseYear.objects.all()
    genres = Genre.objects.all()
    page_number = request.GET.get('page', 1)

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'favourite_list': page_obj,
        'last_comments': last_comments,
        'release_years': release_years,
        'genres': genres,
    }

    return render(request, 'films/user/favourite_list.html', context)


def favourite_post_view(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    if user.id:
        if movie.favourite.filter(id=user.id).exists():
            movie.favourite.remove(user)
        else:
            movie.favourite.add(user)
        return HttpResponseRedirect(movie.get_absolute_url())
    else:
        return redirect('login')
