from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.users.views.forgot_password import forgot_pass_send_email
from apps.users.views.login import login_view
from apps.users.views.register import register_view
from apps.users.views.user_activation import activate
from apps.users.views.user_profile import user_profile_view
from apps.users.views.forgot_password import change_profile_password

urlpatterns = [
    path('user-profile', user_profile_view, name='user_profile'),
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('forgot-password', forgot_pass_send_email, name='forgot-pass-send-email'),
    path('change-profile-password', change_profile_password, name='change_profile_password'),
    path('logout', LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    path('activate-register/<str:uid>/<str:token>',
         activate, name='activate'),
    path('forgot-password/<str:uid>/<str:token>',
         activate, name='forgot-password'),
]
