from django.db.models import Model, ForeignKey, CASCADE, DateTimeField

from root.settings import AUTH_USER_MODEL


class History(Model):
    user = ForeignKey(AUTH_USER_MODEL, CASCADE)
    movie = ForeignKey('movies.Movie', CASCADE)
    view_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-view_at']
