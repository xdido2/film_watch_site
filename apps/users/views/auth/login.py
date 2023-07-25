from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from apps.shared.decorators import anonymous_required
from apps.users.forms.login import LoginForm
from apps.users.models.user import User


@anonymous_required(redirect_url='/')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            user_ = User.objects.filter(email=email).first()
            user = authenticate(email=email, password=password)
            if user_ and not user_.is_active:
                messages.add_message(request,
                                     level=messages.WARNING,
                                     message='user is not active'
                                     )
            elif user:
                login(request, user)
            else:
                messages.add_message(request,
                                     level=messages.ERROR,
                                     message='email or password wrong'
                                     )
                return render(request, 'films/auth/login.html')
            return redirect('movies.film_list_view')
    return render(request, 'films/auth/login.html')
