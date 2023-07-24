from autoslug import AutoSlugField
from django.db.models import ManyToManyField, TextField, FloatField, PositiveIntegerField, ForeignKey, CASCADE
from django.db.models import Model, CharField
from django.urls import reverse


class Movie(Model):
    background_poster = CharField(max_length=255, null=True, blank=True)
    poster = CharField(max_length=255, null=True, blank=True)
    ru_title = CharField(max_length=255)
    orig_title = CharField(max_length=255)
    description = TextField()
    runtime = PositiveIntegerField()
    vote = FloatField()
    vote_count = PositiveIntegerField()
    release_year = ForeignKey('ReleaseYear', on_delete=CASCADE, null=True, blank=True)
    iframe_src = CharField(max_length=255, unique=True)
    translate = CharField(max_length=255, null=True, blank=True)
    max_quality = PositiveIntegerField(null=True, blank=True)
    imdb_id = CharField(max_length=25)
    kinopoisk_id = CharField(max_length=25)
    genre = ManyToManyField('movies.Genre', 'genre', blank=True)
    country = CharField(max_length=255, null=True, blank=True)
    favourite = ManyToManyField('users.User', blank=True)
    slug_link = AutoSlugField(populate_from='ru_title',
                              unique_with=['ru_title'])

    class Meta:
        unique_together = ['ru_title', 'orig_title']
        # ordering = ['-id']

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.slug_link)])

    def __str__(self):
        return self.ru_title


class Genre(Model):
    name = CharField(max_length=255)
    slug_link = AutoSlugField(populate_from='name',
                              unique_with=['name'])

    def __str__(self):
        return self.name


class ReleaseYear(Model):
    year = PositiveIntegerField()

    class Meta:
        ordering = ['-year']
