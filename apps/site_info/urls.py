from django.urls import path

from apps.site_info.views.feedback import feedback_view

urlpatterns = [
    path('feedback/', feedback_view, name='feedback'),
]
