from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index_view'),
    path('test/', test, name='test_view'),
]