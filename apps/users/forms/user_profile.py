from django.forms import Form, CharField


class UserProfileForm(Form):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email
