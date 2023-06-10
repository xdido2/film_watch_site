from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from apps.users.forms.reset_password import ResetPassword
from apps.users.token_gen import account_activation_token


def activate(request, uid, token):
    User = get_user_model()

    url_name = request.resolver_match.url_name

    try:
        uuid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uuid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token) and url_name == 'activate':
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    elif user is not None and account_activation_token.check_token(user, token) and url_name == 'forgot-password':
        if request.method == 'POST':
            forms = ResetPassword(request.POST)
            if forms.is_valid():
                user.password = make_password(request.POST['password'])
                user.save()
                return redirect('login')

            else:
                context = {
                    'errors': forms.errors,
                    'uid': uid,
                    'token': token}
                return render(request, 'films/auth/forgot_password_code.html', context)

        return render(request, 'films/auth/forgot_password_code.html', {'uid': uid, 'token': token})
    else:
        return HttpResponse('Activation link is invalid!')
