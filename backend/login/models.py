from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from uk_geo_utils.helpers import Postcode


# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, postcode, email, password=None, ):
        if not email:
            raise ValueError('users must have a email address!')

        email = self.normalize_email(email)
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.save()

        return user

    def create_student(self,first_name, last_name, username, birthdate, password = None):
        if not username:
            raise ValueError('Username already exists!')

        student = self.model(username=username,password=password)
        student.set_password(password)
        student.save()

        return student


class UserAccount(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    username = models.CharField(max_length=30, unique=True, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'postcode','username']

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_full_name(self):
        return self.last_name, self.last_name

    def __str__(self):
        return self.email





