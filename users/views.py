from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .form import SignUpForm


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/sign_up.html'
