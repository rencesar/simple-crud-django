from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'clients'
urlpatterns = [
    path('add/', views.ClientCreateView.as_view(), name='create-client'),
    path('', views.ClientListView.as_view(), name='list-client'),
    path('<uuid:pk>/', views.ClientDetailView.as_view(), name='detail-client'),
    path('edit/<uuid:pk>/', views.ClientUpdateView.as_view(), name='update-client'),
    path('success/', TemplateView.as_view(template_name='success-client.html'), name='success-client'),
]
