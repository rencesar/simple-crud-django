from django.urls import path

from . import views


urlpatterns = [
    path('add/', views.ClientCreateView.as_view(), name='create-client'),
    path('', views.ClientListView.as_view(), name='list-client'),
]
