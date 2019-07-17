from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'replies', views.ReplyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    ]
