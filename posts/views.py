from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'

    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_list(request, group_id: str):
    template = 'posts/group_list.html'

    group = get_object_or_404(Group, slug=group_id)
    group_posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'group_posts': group_posts,
    }
    return render(request, template, context)
