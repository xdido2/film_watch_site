from django.shortcuts import get_object_or_404, redirect

from apps.movies.forms.comment import CommentForm
from apps.movies.models.movie import Movie


def post_comment(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.movie = movie
        comment.save()
        return redirect('movie_detail', movie_id)
