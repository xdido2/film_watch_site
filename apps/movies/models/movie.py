from autoslug import AutoSlugField
from django.db.models import ManyToManyField
from django.db.models import Model, CharField, ForeignKey, CASCADE, ImageField


class Movie(Model):
    ru_title = CharField(max_length=255)
    orig_title = CharField(max_length=255)
    released = CharField(max_length=15, null=True, blank=True)
    iframe_src = CharField(max_length=255, unique=True)
    imdb_id = CharField(max_length=25)
    kinopoisk_id = CharField(max_length=25)
    genre = ManyToManyField('movies.Genre', 'ganre', blank=True)
    slug_link = AutoSlugField(populate_from='orig_title',
                              unique_with=['orig_title'])

    class Meta:
        ordering = ['-id']
        unique_together = ['ru_title', 'orig_title']

    def __str__(self):
        return self.ru_title


class Previews(Model):
    image = ImageField(upload_to='media')
    movie = ForeignKey('Movie', CASCADE, 'images')


class Genre(Model):
    name = CharField(max_length=255)
    slug_link = AutoSlugField(populate_from='name',
                              unique_with=['name'])

    def __str__(self):
        return self.name
