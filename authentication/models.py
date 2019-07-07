from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    name = models.CharField(_('Name'), max_length=120, blank=True)
    email = models.EmailField(_('email address'), blank=False, null=False, unique=True)
    first_name = None
    last_name = None
