from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here
class UserManager(BaseUserManager):
    def create_user(self, username, password):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not username:
            raise ValueError('User must have an username')

        if not password:
            raise ValueError('User must have an password')

        user = self.model(
            name = username,
            password = password
        )
    
    def create_superuser(self, username, password):
        """
        Creates and saves a User with the given email, name, tc and password.
        """


class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __srt__(self):
        return self.username