from django.db.models import EmailField, Model, TextField, URLField


class Settings(Model):
    owner_email = EmailField(max_length=125)
    django_email = EmailField()
    about_us = TextField()
    youtube_link = URLField(null=True, blank=True)
    vk_link = URLField(null=True, blank=True)
    facebook_link = URLField(null=True, blank=True)
    telegram_link = URLField(null=True, blank=True)
