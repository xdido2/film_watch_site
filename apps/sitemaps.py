from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.movies.models.movie import Movie


class MovieSitemap(Sitemap):
    priority = 1.0  # Modify this according to the priority of your movie pages

    def items(self):
        return Movie.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('film-detail',
                       args=[obj.slug_link])
