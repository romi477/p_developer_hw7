from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin


admin.site.register(MyUser, UserAdmin)

admin.site.site_url = 'http://127.0.0.1:8888/hasker/'
