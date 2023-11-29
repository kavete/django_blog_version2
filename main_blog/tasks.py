from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_newsletter(subscriber_email):
    newsletter_subject = "Your Newsletter Subject"
    newsletter_message = "Your newsletter content goes here."

    send_mail(
        newsletter_subject,
        newsletter_message,
        settings.DEFAULT_FROM_EMAIL,
        [subscriber_email],
        fail_silently=False,
    )
