from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'

    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    current_page_posts = paginator.get_page(page_number)

    context = {
        'current_page_posts': current_page_posts,
    }
    return render(request, template, context)


def group_list(request, slug: str):
    template = 'posts/group_list.html'

    group = get_object_or_404(Group, slug=slug)
    group_posts = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(group_posts, 5)

    page_number = request.GET.get('page')
    current_page_posts = paginator.get_page(page_number)

    context = {
        'group': group,
        'current_page_posts': current_page_posts,
    }
    return render(request, template, context)
