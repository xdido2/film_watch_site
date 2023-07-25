from django_filters import FilterSet

from apps.movies.models.movie import Movie


class ProductFilter(FilterSet):
    class Meta:
        model = Movie
        fields = ['release_date']
