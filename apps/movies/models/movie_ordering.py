from django.db.models import Model, EmailField, URLField, TextField, CharField


class Order(Model):
    email = EmailField()
    content_title = CharField()
    content_url = URLField()
    content_description = TextField()


