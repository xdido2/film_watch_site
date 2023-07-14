from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models.favourite import Favourite
from apps.movies.models import Movie
from apps.users.serializers.favourite_serializer import FavouriteSerializer


class FavouriteCreateDestroyView(DestroyAPIView, ListCreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return Favourite.objects.filter(user_id=self.request.user.pk)

    def post(self, request, *args, **kwargs):
        try:
            movie_id = request.data['movie']
            user = request.user
            if not Favourite.objects.filter(user=user.pk, movie_id=movie_id).exists():
                favourite = Favourite.objects.create(movie_id=movie_id, user_id=user.pk)
                movie = get_object_or_404(Movie, pk=movie_id)
                movie.favourites_count += 1
                movie.save()
                favourite.save()
                return Response({'success': 'Movie is added to your favourite library!'},
                                status=status.HTTP_201_CREATED)
            return Response({'error': 'Movie is already in your favourite library!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Movie id and user id are required!'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            movie_id = request.data['movie']
            user = request.user
            if Favourite.objects.filter(user=user.pk, movie_id=movie_id).exists():
                Favourite.objects.filter(user=user.pk, movie_id=movie_id).delete()
                movie = get_object_or_404(Movie, movie_id=movie_id)
                movie.favourites_count -= 1
                movie.save()
                return Response({'success': 'Movie removed from favourite library'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'This movie is already removed from favourite library!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Movie id and user id are required!'}, status=status.HTTP_400_BAD_REQUEST)
