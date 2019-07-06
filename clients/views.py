from django.views import generic
from django.urls import reverse_lazy

from .forms import ClientForm


class ClientListView(generic.TemplateView):
    template_name = 'list-clients.html'


class ClientCreateView(generic.CreateView):
    form_class = ClientForm
    template_name = 'create-clients.html'
    success_url = reverse_lazy('clients:success-client')
