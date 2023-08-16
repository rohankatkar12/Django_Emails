from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import send_email_to_student

def index(request):
    title = "Send E-mail to Student"
    return render(request, 'email.html', {'title':title})

def send_email(request):
    send_email_to_student()
    return redirect('/')


