from django.db.models import Model, TextField, CharField


class Faq(Model):
    question = CharField(max_length=255)
    text = TextField()
