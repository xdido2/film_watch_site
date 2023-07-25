from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from apps.shared.tasks.send_email_task import send_feedback_email
from apps.site_info.models.about import Settings


def feedback_view(request):
    data = Settings.objects.first()
    context = {
        'site_info': data,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', 'Contact Form Submission')
        message = request.POST.get('message')

        # Build the email message
        context = {
            'name': name,
            'email': email,
            'message': message,
            'site_info': {'email': data.owner_email},  # Replace with your email address
        }
        email_message = render_to_string('email/feedback-email.html', context)

        send_feedback_email(
            subject=subject,
            email_message=email_message,
            email=email,
            data=data,
        )
        return redirect('feedback')
    return render(request, 'films/site-info/contact-form.html', context)
