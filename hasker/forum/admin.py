from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question

admin.site.register(Question)


admin.site.site_url = 'http://127.0.0.1:8888/hasker/'
