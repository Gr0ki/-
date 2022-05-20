from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm


class AccountView(LoginRequiredMixin, TemplateView):
    template_name='accounts/account_page.html'
    login_url='login/'


# class AdminView(PermissionRequiredMixin, TemplateView):
#     template_name='accounts/admin.html'
#     permission_required='is_admin'
#     raise_exception = True  # Raise exception when no access instead of redirect
#     permission_denied_message = "You are not an admin!"


class LoginView(TemplateView):
    template_name='accounts/login.html'


class RegisterView(TemplateView):
    template_name='accounts/register.html'


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CreateUserForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)
