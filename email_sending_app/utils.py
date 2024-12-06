from django.conf import settings
from django.core.mail import send_mail  # Use the built-in send_mail function

def send_email_to_client():
    subject = "Your Email Subject"  # Set a proper subject
    message = "Your message content here"  # Set the content of the message
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["xyz@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)
