from django.db.models import CharField, EmailField, Model


class Settings(Model):
    phone = CharField(max_length=25)
    email = EmailField(max_length=125)
    about_us = CharField(max_length=512)
