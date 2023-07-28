from django.forms import ModelForm

from apps.movies.models.movie_ordering import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
