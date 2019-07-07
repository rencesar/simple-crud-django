from django.urls import reverse_lazy
from django.views import generic

from authentication.forms import CustomUserCreationForm


class CreateUserAccountView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'create-account.html'

