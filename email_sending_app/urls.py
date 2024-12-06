from django.urls import path
from .views import homepage, send_email

urlpatterns = [
    path('', homepage, name='homepage'),
    path('send-email/', send_email, name='send_email'),  # Add this path
]
