from django import forms

from .models import Clients


class ClientForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = ('name', 'phone', 'zipcode', 'address', 'number', 'city', 'state')

