from django.contrib import admin
from django.urls import path, include
from .views import redirect_index
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', redirect_index),
    path('admin/', admin.site.urls),
    path('hasker/', include('forum.urls')),
    path('hasker/auth/', include('authorization.urls')),
] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
