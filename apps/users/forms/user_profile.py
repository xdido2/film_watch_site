from django.forms import Form

from apps.users.models import User


class UserProfileForm(Form):
    class Meta:
        model = User
        fields = ('avatar',)

