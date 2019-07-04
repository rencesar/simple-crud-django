from django.views.generic import TemplateView


class ClientListView(TemplateView):
    template_name = 'list-clients.html'
