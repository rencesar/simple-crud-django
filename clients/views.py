from django.views import generic

from .models import Clients


class ClientListView(generic.TemplateView):
    template_name = 'list-clients.html'


class ClientCreateView(generic.CreateView):
    model = Clients
    template_name = 'create-clients.html'
    fields = ['name', 'phone', 'address', 'number', 'city', 'state', 'zipcode',]
