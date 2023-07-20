from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.users.views.auth.forgot_password import change_profile_password
from apps.users.views.auth.forgot_password import forgot_pass_send_email
from apps.users.views.auth.login import login_view
from apps.users.views.auth.register import register_view
from apps.users.views.auth.user_activation import activate
from apps.users.views.user.user_profile import user_profile_view
from apps.users.views.user.favourite import favourite_post_view, favourite_list_view

urlpatterns = [
    path('user-profile', user_profile_view, name='user_profile'),
    path('favourite_list/', favourite_list_view, name='favourite_list'),
    path('favourite_post/<int:movie_id>', favourite_post_view, name='favourite_post'),
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
