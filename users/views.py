from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from .form import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/sign_up.html'


@method_decorator(login_required, name='dispatch')
class ProtectedLogoutView(auth_views.LogoutView):
    pass
