from django.db.models import EmailField, Model, TextField


class Settings(Model):
    email = EmailField(max_length=125)
    about_us = TextField()
