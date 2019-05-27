from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return HttpResponse(f'<div>{request.method}</div>\n\n{request.environ}')


def index(request):
    return render(request, 'forum/index.html', {})