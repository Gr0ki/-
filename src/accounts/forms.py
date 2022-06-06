from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

# from django import forms
from captcha.fields import CaptchaField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]    


class AuthUserForm(AuthenticationForm):
    captcha = CaptchaField()


class ChangePasswordForm(PasswordChangeForm):
    pass
