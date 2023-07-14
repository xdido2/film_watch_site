from django.db.models import Model, ForeignKey, CASCADE

from root.settings import AUTH_USER_MODEL


class Favourite(Model):
    user = ForeignKey(AUTH_USER_MODEL, CASCADE)
    movie = ForeignKey('movies.Movie', CASCADE)
