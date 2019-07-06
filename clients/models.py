from django.db import models

from django.utils.translation import gettext as _


class Clients(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    phone = models.CharField(_('Phone number'), max_length=20)
    address = models.CharField(_('Address'), max_length=150)
    number = models.CharField(_('Street number'), max_length=20)
    city = models.CharField(_('City'), max_length=50)
    state = models.CharField(_('State'), max_length=35)
    zipcode = models.CharField(_('Zip code'), max_length=25)
