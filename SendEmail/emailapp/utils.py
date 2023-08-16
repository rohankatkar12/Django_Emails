from django.core.mail import send_mail
from django.conf import settings

def send_email_to_student():
    subject = "This email is from Django Server"
    message = "Congratulation!! You are registered in our django system."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['rohankatkar1212@gmail.com']
    send_mail(subject, message, from_email, recipient_list)