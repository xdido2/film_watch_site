from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput

from apps.users.models.user import User


class RegisterForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and self._meta.model.objects.filter(username=username).exists():
            self._update_errors(
                ValidationError(
                    {
                        "username": 'Пользователь с таким никнеймом уже есть!'
                    }
                )
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and self._meta.model.objects.filter(email__iexact=email).exists():
            self._update_errors(
                ValidationError(
                    {
                        "email": 'Пользователь с такой почтой уже есть!'
                    }
                )
            )
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Password do not match")
        # password_validation.validate_password(password)
        return make_password(password)
