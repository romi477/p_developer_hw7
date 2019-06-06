from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person, PersonalProfile, Test

admin.site.register(Person, UserAdmin)
admin.site.register(PersonalProfile)
admin.site.register(Test)

