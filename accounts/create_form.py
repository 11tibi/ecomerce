from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUser(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1']
