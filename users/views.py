from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .form import SignUpForm


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('posts:index')
