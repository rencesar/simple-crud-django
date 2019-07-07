from django.views import generic
from django.urls import reverse_lazy

from .forms import ClientForm
from .models import Clients


class ClientListView(generic.ListView):
    template_name = 'list-clients.html'
    model = Clients


class ClientCreateView(generic.CreateView):
    form_class = ClientForm
    template_name = 'create-clients.html'
    success_url = reverse_lazy('clients:success-client')
