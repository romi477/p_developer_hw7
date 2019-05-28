from django.contrib import admin
from django.urls import path, include
from .views import redirect_index

urlpatterns = [
    path('', redirect_index),
    path('admin/', admin.site.urls),
    path('hasker/', include('forum.urls')),
    path('hasker/auth/', include('authorization.urls')),
]
