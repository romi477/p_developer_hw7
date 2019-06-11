from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person, Test

admin.site.register(Person, UserAdmin)
admin.site.register(Test)

