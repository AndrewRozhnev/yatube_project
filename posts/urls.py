from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:group_id>/', views.group_posts),
]