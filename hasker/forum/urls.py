from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index_view'),
    path('test/', test, name='test_view'),
    path('tags/', TagListView.as_view(), name='tags_view'),
    path('tags/<tag>/', tag_questions, name='tag_questions_list'),
    path('addquestion/', QuestionCreate.as_view(), name='add_question'),
    path('question/<slug>/', QuestionDetail.as_view(), name='question_detail'),
    path('addanswer/', AnswerCreate.as_view(), name='add_answer'),
]