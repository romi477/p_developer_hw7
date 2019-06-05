from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Test

admin.site.register(UserProfile)
admin.site.register(Test)

