from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',

        ]

    username = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Username',
            }
        )
    )

    password1 = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )

    password2 = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Re-enter the password',
            }
        )
    )
