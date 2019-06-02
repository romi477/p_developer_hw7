from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index_view'),
    path('test/', test, name='test_view'),
    path('users/<username>/', UserInfo.as_view(), name='personal_info'),
    path('users/', users, name='users_view')
]