from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect

from shared.utils.send_to_email import send_email
from users.forms.register import RegisterForm
from users.forms.reset_password import ResetPasswordEmail


def forgot_pass_send_email(request):
    context = {}
    domain = get_current_site(request).domain
    if request.method == 'POST':
        forms = ResetPasswordEmail(request.POST)
        if forms.is_valid():
            send_email.delay(domain, forms.data.get('email'), type_='forgot_password')
            return redirect('login')
        else:
            context['errors'] = forms.errors
    return render(request, 'films/auth/forgot_password_email.html', context)


