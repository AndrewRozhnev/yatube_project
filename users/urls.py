from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html',
                                      redirect_authenticated_user=True), name='login'),

    path('logout/',
         views.ProtectedLogoutView.as_view(template_name='users/logged_out.html'), name='logout'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html',
                                               success_url=reverse_lazy('users:pass_change_done')),
         name='pass_change_form'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='pass_change_done'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                              success_url=reverse_lazy('users:pass_reset_done')),
         name='pass_reset_form'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='pass_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                     success_url=reverse_lazy('users:reset_complete')),
         name='reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='reset_complete'),
]
