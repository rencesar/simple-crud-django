from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField('Name', max_length=120, blank=True)
    first_name = None
    last_name = None
