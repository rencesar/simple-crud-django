from django.contrib import admin

from . import models


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'city', 'state')


admin.site.register(models.Client, ClientsAdmin)
