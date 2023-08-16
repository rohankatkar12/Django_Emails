from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .utils import send_email_to_student, email_with_attachment


def index(request):
    title = "Send E-mail to Student"
    return render(request, 'email.html', {'title':title})

def send_email(request):
    send_email_to_student()
    return redirect('/')

def send_email_with_attachment(request):
    subject = "This email is from Django Server with attchment"
    message = "Hey please find this attach file with this email"
    recipient_list = ['rohankatkar1212@gmail.com']
    file_path = f"{settings.BASE_DIR}/static/test.pdf"
    email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')


