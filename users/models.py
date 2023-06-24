from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
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
            username = self.normalize_username(username)
        )

        user.set_password(password)

        user.save()

        return user


    def create_superuser(self, username, password):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not username:
            raise ValueError('User must have an username')

        if not password:
            raise ValueError('User must have an password')

        user = self.model(
            username = self.normalize_username(username)
        )

        user.set_password(password)

        user.is_staff = True

        user.is_superuser = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username