from django.urls import path

from . import views


urlpatterns = [
    path(r'^$', views.ClientListView.as_view(), name='client-list'),
]
