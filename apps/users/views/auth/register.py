from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect

from apps.shared.decorators import anonymous_required
from apps.shared.utils.send_to_email import send_email
from apps.users.forms.register import RegisterForm


@anonymous_required(redirect_url='/')
def register_view(request):
    context = {}
    domain = get_current_site(request).domain
    protocol = request.scheme
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            # send_email.delay(protocol, domain, forms.data.get('email'), type_='register')
            forms.save()
            return redirect('login')
        else:
            context['errors'] = forms.errors
    return render(request, 'films/auth/register.html', context)
