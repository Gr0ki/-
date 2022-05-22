from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm, AuthUserForm


class AccountView(LoginRequiredMixin, TemplateView):
    template_name='accounts/account_page.html'
    login_url='login/'


# class AdminView(PermissionRequiredMixin, TemplateView):
#     template_name='accounts/admin.html'
#     permission_required='is_admin'
#     raise_exception = True  # Raise exception when no access instead of redirect
#     permission_denied_message = "You are not an admin!"


# class LoginView(TemplateView):
#     template_name='registration/login.html'


# class RegisterView(TemplateView):
#     template_name='registration/register.html'


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):
    form = AuthUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.info(request, 'Username or password is incorrect.')
            context = {}
            return render(request, 'registration/login.html')

    context = {'form': form}
    return render(request, 'registration/login.html', context)
