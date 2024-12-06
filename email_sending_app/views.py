from django.shortcuts import render, redirect
from .utils import send_email_to_client

def homepage(request):
    return render(request, 'index.html')

def send_email(request):
    send_email_to_client()  # Call the email sending function
    return redirect('homepage')  # Redirect to homepage or another page
