from django.db.models import Model, EmailField, URLField, TextField, CharField


class Order(Model):
    email = EmailField()
    content_title = CharField(max_length=255)
    content_url = URLField()
    content_description = TextField()


