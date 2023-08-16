from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_to_student():
    subject = "This email is from Django Server"
    message = "Congratulation!! You are registered in our django system."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['rohankatkar1212@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


def email_with_attachment(subject, message, recipient_list, file_path):
    email = EmailMessage(
        subject = subject,
        body = message,
        from_email = settings.EMAIL_HOST_USER,
        to = recipient_list
    )
    email.attach_file(file_path)
    email.send()