from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:group_id>/', views.group_posts, name='group_posts'),
]
