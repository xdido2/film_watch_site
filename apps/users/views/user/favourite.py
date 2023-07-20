from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from apps.movies.models.movie import Movie


def favourite_list_view(request):
    user = request.user
    favourite_list = user.movie_set.all()
    context = {
        'favourite_list': favourite_list,
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
