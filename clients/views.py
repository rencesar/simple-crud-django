from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.decorators import method_decorator

from .forms import ClientForm
from .models import Client


@method_decorator(login_required, name='dispatch')
class ClientListView(generic.ListView):
    template_name = 'list-clients.html'
    model = Client


@method_decorator(login_required, name='dispatch')
class ClientCreateView(generic.CreateView):
    form_class = ClientForm
    template_name = 'form-clients.html'
    success_url = reverse_lazy('clients:success-client')
    extra_context = {'operation': _('Add'), 'is_edit': False}


@method_decorator(login_required, name='dispatch')
class ClientUpdateView(generic.UpdateView):
    form_class = ClientForm
    model = Client
    template_name = 'form-clients.html'
    success_url = reverse_lazy('clients:success-client')
    extra_context = {'operation': _('Edit'), 'is_edit': True}


@method_decorator(login_required, name='dispatch')
class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'detail-clients.html'
    success_url = reverse_lazy('clients:success-client')


@method_decorator(login_required, name='dispatch')
class ClientDeleteView(generic.DeleteView):
    model = Client
    template_name = 'delete-clients.html'
    success_url = reverse_lazy('clients:success-client')
