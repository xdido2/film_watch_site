from django.core.exceptions import ValidationError
from django.forms import Form
from django.shortcuts import get_object_or_404

from users.models.user import User


class LoginForm(Form):
    def clean_password(self):
        email = self.data.get('email')
        password = self.data.get('password')
        user = get_object_or_404(User, email=email)
        if user.check_password(password):
            raise ValidationError("Password or Username Do Not Match")
        return password
