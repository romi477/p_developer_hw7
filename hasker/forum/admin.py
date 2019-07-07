from django.contrib import admin
from .models import Question, Reply, Tag

admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(Tag)

admin.site.site_url = '/hasker/'
