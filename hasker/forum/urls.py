from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tags/<tag_name>/', tag_questions, name='tag_questions'),
    path('add-question/', QuestionCreate.as_view(), name='add_question'),
    path('question/<slug>/', QuestionDetail.as_view(), name='question_detail'),
    path('question/<slug>/add-reply/', ReplyCreate.as_view(), name='add_reply'),
    path('question/<slug>/<reply_pk>/', add_medal, name='add_medal'),
    
    path('question/<slug>/<reply_pk>/like/', like, name='like'),
    path('question/<slug>/<reply_pk>/dislike/', dislike, name='dislike')
]