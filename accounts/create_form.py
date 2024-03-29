from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateUser(UserCreationForm):
    password2 = None

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1']
