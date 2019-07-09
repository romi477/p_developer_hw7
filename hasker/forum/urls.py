from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index_view'),
    path('tags/', TagListView.as_view(), name='tags_view'),
    path('tags/<tag>/', tag_questions, name='tag_questions_list'),
    path('add-question/', QuestionCreate.as_view(), name='add_question'),
    path('question/<slug>/', QuestionDetail.as_view(), name='question_detail'),
    path('question/<slug>/add-reply/', ReplyCreate.as_view(), name='add_reply'),
    path('question/<slug>/<pk>/', add_medal, name='add_medal'),
    
    path('question/<slug>/<pk>/like/', like, name='like'),
    path('question/<slug>/<pk>/dislike/', dislike, name='dislike')
]