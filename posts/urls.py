from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_detail, name='group_detail'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
