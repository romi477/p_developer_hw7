from django.urls import path
from .views import *


urlpatterns = [
    path('test/', test, name='test_view'),
    path('index/', index, name='index_view')
]