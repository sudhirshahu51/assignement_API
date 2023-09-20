# authentication/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import UserCredentials

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserCredentials.objects.get(username=username)
            if user.password == password:
                return user
        except UserCredentials.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserCredentials.objects.get(pk=user_id)
        except UserCredentials.DoesNotExist:
            return None
