from django.http import HttpResponse


def index(request):
    return HttpResponse('Homepage')


def group_posts(request, group_id: str):
    return HttpResponse(f'{group_id.title()} group posts')
