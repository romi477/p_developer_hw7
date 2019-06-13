from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Tag


class TagListView(ListView):
    model = Tag
    template_name = 'forum/tag_list.html'
    context_object_name = 'tag_list'
    


def test(request):
    return HttpResponse(f'<div>{request.method}</div>\n\n{request.environ}')

def index(request):
    return render(request, 'forum/index.html', {})

def AskQuestion():
    pass
