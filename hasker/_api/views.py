from rest_framework import viewsets, permissions
from forum.models import Question, Reply
from .serializers import QuestionSerializer, ReplySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # def get_queryset(self, *args, **kwargs):
    #     return Reply.objects.filter(author__username=self.request.user.username)
    
    