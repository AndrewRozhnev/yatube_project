from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('group/<slug:slug>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:post_id>/update/', views.PostUpdateView.as_view(), name='post_update'),
]
