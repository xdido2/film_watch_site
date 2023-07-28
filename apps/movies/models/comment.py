from django.db.models import Model, ForeignKey, CASCADE, DateTimeField, TextField, BooleanField

from root.settings import AUTH_USER_MODEL


class Comment(Model):
    user = ForeignKey(AUTH_USER_MODEL, CASCADE)
    movie = ForeignKey('movies.Movie', CASCADE)
    content = TextField(max_length=300)
    is_approved = BooleanField(default=False, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.ru_title} - {self.content}'

    class Meta:
        ordering = ['-created_at']
