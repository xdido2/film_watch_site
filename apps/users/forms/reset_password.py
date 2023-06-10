from django.core.exceptions import ValidationError
from django.forms import Form


class ResetPasswordEmail(Form):
    def clean_email(self):
        email = self.data.get('email')


class ResetPassword(Form):
    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password Do Not Match')
