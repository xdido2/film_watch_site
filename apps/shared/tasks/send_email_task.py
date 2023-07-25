from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.users.models.user import User
from apps.users.token_gen import account_activation_token
from root.settings import EMAIL_HOST_USER


@shared_task
def send_email(protocol, domain, email, type_):
    user = get_object_or_404(User, email=email)
    subject = 'Activate your account'
    from_email = EMAIL_HOST_USER
    recipient_list = [email]
    if type_ == 'register':
        message = render_to_string('email/activate-account-for-register.html', {
            'user': user.username,
            'protocol': protocol,
            'domain': domain,
            'uidb64': urlsafe_base64_encode(force_bytes(str(user.pk))),
            'token': account_activation_token.make_token(user)
        })
        send_mail(subject, message, from_email, recipient_list)

    elif type_ == 'forgot_password':
        message = render_to_string('email/activate-account-for-forgot-password.html', {
            'user': user,
            'protocol': protocol,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
            'token': account_activation_token.make_token(user)
        })
        send_mail(subject, message, from_email, recipient_list)


@shared_task
def send_feedback_email(subject, email_message, email, data):
    send_mail(
        subject=subject,
        message=email_message,
        from_email=email,
        recipient_list=[data.owner_email],  # Replace with your email address
    )
