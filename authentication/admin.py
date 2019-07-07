from django.contrib import admin

from . import models


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_joined')


admin.site.register(models.User, ClientsAdmin)
