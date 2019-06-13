from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index_view'),
    path('test/', test, name='test_view'),
    path('tags/', TagListView.as_view(), name='tags_view'),
    # path('question/', AskQuestion, name='question'),
]