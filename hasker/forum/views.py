from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import MyUser
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.views import View


def test(request):
    return HttpResponse(f'<div>{request.method}</div>\n\n{request.environ}')


def index(request):
    return render(request, 'forum/index.html', {})


class UserInfo(View):
    def get(self, request, username):
        person = get_object_or_404(MyUser, username=username)
        return render(request, 'forum/user_info.html', {'user': person})


def users(request):
    persons = User.objects.all()
    return render(request, 'forum/all_users.html', {'users': persons})
