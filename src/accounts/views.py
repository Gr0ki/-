from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from .forms import *


class AccountView(LoginRequiredMixin, TemplateView):
    template_name='accounts/account_page.html'
    login_url='login/'


def register_request(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_request(request):
    form = AuthUserForm()

    if request.method == 'POST':
        form = AuthUserForm(request, data=request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('account')
            else:
                messages.info(request, 'User has been banned.')
        else:
            messages.info(request, 'Username or password is incorrect.')

    form = AuthUserForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def logout_request(request):
    logout(request)
    return redirect("welcome")

@login_required
def change_password_request(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account')
    else:
        form = ChangePasswordForm(request.user)
    context = {'form': form}
    return render(request, 'registration/change_password.html', context)
