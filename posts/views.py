from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

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
