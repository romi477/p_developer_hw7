from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('hot-questions/', hot_questions, name='hot_questions'),
    path('tags/<tag_name>/', tag_questions, name='tag_questions'),
    path('add-question/', QuestionCreate.as_view(), name='add_question'),
    path('question/<slug>/', QuestionDetail.as_view(), name='question_detail'),

    path('question/<slug>/like/', like, name='question_like'),
    path('question/<slug>/dislike/', dislike, name='question_dislike'),

    path('question/<slug>/add-reply/', ReplyCreate.as_view(), name='add_reply'),

    path('question/<slug>/<int:reply_pk>/medal/', add_medal, name='add_medal'),
    path('question/<slug>/<int:reply_pk>/like/', like, name='reply_like'),
    path('question/<slug>/<int:reply_pk>/dislike/', dislike, name='reply_dislike')
]