from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
