from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views.forgot_password import forgot_pass_send_email
from users.views.login import login_view
from users.views.register import register_view
from users.views.user_activation import activate

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('forgot-password', forgot_pass_send_email, name='forgot-pass-send-email'),
    path('logout', LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    path('activate-register/<str:uid>/<str:token>',
         activate, name='activate'),
    path('forgot-password/<str:uid>/<str:token>',
         activate, name='forgot-password'),
]
