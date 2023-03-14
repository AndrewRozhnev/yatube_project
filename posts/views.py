from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PostForm
from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    current_page_posts = paginator.get_page(page_number)

    context = {
        'current_page_posts': current_page_posts,
    }
    template = 'posts/index.html'

    return render(request, template, context)


def group_detail(request, slug: str):
    group = get_object_or_404(Group, slug=slug)
    group_posts = Post.objects.filter(group=group).order_by('-pub_date')

    paginator = Paginator(group_posts, 5)
    page_number = request.GET.get('page')
    current_page_posts = paginator.get_page(page_number)

    context = {
        'group': group,
        'current_page_posts': current_page_posts,
    }
    template = 'posts/group_detail.html'

    return render(request, template, context)


@login_required
def user_profile(request, username: str):
    current_user = get_object_or_404(get_user_model(), username=username)
    user_posts = Post.objects.filter(author=current_user).order_by('-pub_date')

    paginator = Paginator(user_posts, 5)
    page_number = request.GET.get('page')
    current_page_posts = paginator.get_page(page_number)

    context = {
        'current_user': current_user,
        'current_page_posts': current_page_posts,
    }
    template = 'posts/user_profile.html'

    return render(request, template, context)


def post_detail(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post': post,
    }
    template = 'posts/post_detail.html'

    return render(request, template, context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.instance.author = request.user
        form.instance.author_id = request.user.id

        if form.is_valid():
            form.save()
            return redirect(reverse('posts:user_profile', kwargs={'username': request.user}))
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    template = 'posts/post_create.html'

    return render(request, template, context)


@login_required
def post_edit(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect(reverse('posts:post_detail', kwargs={'post_id': post_id}))

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect(reverse('posts:user_profile', kwargs={'username': request.user}))
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }
    template = 'posts/post_edit.html'

    return render(request, template, context)
