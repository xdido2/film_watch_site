from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from apps.movies.models.movie import Movie


def favourite_list_view(request):
    user = request.user
    favourite_list = user.movie_set.all()
    p = Paginator(favourite_list, 10)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    page_obj.adjusted_elided_pages = p.get_elided_page_range(page_number)

    context = {
        'favourite_list': page_obj,
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
