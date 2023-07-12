from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm
from django.shortcuts import get_object_or_404

from apps.users.models import User


class ResetPasswordEmail(Form):
    def clean_email(self):
        email = self.data.get('email')


class ResetPassword(Form):
    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password Do Not Match')


class ChangeProfilePassword(ModelForm):
    class Meta:
        model = User
        fields = ('password',)

    def clean_password(self):
        password = self.data.get('password')
        old_password = self.data.get('old_password')
        confirm_password = self.data.get('confirm_password')
        if self.instance.check_password(old_password):
            if password != confirm_password:
                raise ValidationError("Password do not match")
            # password_validation.validate_password(password)
            return make_password(password)
        raise ValidationError('Old password is incorrect')
