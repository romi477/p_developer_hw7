from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('question/<str:slug>/', views.question_detail),
    path('question/<str:slug>/replies/', views.question_replies),
    ]
