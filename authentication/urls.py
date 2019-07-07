from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views

app_name = 'authentication'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html', success_url=reverse_lazy('clients:success-client')),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
