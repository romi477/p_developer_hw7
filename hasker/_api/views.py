from rest_framework import viewsets, permissions
from django.apps import apps
from .serializers import QuestionSerializer, ReplySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    model_obj = apps.get_model('forum', 'Question')
    queryset = model_obj.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReplyViewSet(viewsets.ModelViewSet):
    model_obj = apps.get_model('forum', 'Reply')
    queryset = model_obj.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # def get_queryset(self, *args, **kwargs):
    #     return self.model_obj.objects.filter(author__username=self.request.user.username)
    
    