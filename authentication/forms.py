from django.contrib.auth.forms import UserCreationForm

from authentication.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('name', 'email')

