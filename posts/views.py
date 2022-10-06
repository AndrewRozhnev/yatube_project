from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    content = 'Это главная страница проекта YaTube'
    context = {
        'content': content,
    }
    return render(request, template, context)


def group_posts(request, group_id: str):
    template = 'posts/group_list.html'
    content = f'Скоро здесь будет информация о {group_id} группе проекта YaTube'
    context = {
        'content': content,
        'group_id': group_id,
    }
    return render(request, template, context)
