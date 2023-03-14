from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/sign_up.html'


class ProtectedLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    ...
