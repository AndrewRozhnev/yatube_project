from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django_jinja.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Group, Post

User = get_user_model()


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'posts/index.html'


class GroupDetailView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'posts/group_detail.html'

    def get_queryset(self):
        self.group = get_object_or_404(Group, slug=self.kwargs['slug'])
        return Post.objects.filter(group=self.group).order_by('-pub_date')


class UserProfileView(LoginRequiredMixin, ListView):
    paginate_by = 5
    template_name = 'posts/user_profile.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=self.user).order_by('-pub_date')


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:user_profile', kwargs={'username': self.request.user})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_update.html'
    pk_url_kwarg = 'post_id'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def handle_no_permission(self):
        # Redirect to the post detail view if the test_func is not passed
        post_id = self.kwargs['post_id']
        return redirect('posts:post_detail', post_id=post_id)

    def get_success_url(self):
        return reverse_lazy('posts:user_profile', kwargs={'username': self.request.user})
