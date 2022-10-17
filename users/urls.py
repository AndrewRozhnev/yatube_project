from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView,
                                       PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('login/',
         LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=False), name='login'),

    path('logout/',
         LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),

    path('password_change/',
         PasswordChangeView.as_view(template_name='users/password_change_form.html',
                                    success_url=reverse_lazy('users:pass_change_done')),
         name='pass_change_form'),

    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='pass_change_done'),

    path('password_reset/',
         PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                   success_url=reverse_lazy('users:pass_reset_done')),
         name='pass_reset_form'),

    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='pass_reset_done'),

    path('password_reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url=reverse_lazy('users:pass_reset_complete')),
         name='pass_reset_confirm'),

    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='pass_reset_complete'),
]
