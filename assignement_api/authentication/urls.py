# authentication/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),  # Use Django REST framework's obtain_auth_token view
]
