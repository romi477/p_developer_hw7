from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person, PersonProfile, Test

admin.site.register(Person, UserAdmin)
admin.site.register(PersonProfile)
admin.site.register(Test)

