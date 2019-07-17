from rest_framework import status
from forum.models import Question, Reply
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer, ReplySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['GET', 'DELETE'])
def question_detail(request, slug):
    try:
        question = Question.objects.get(slug=slug)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def question_replies(request, slug):
    try:
        question = Question.objects.get(slug=slug)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        replies = Reply.objects.filter(related_q__slug=question.slug).order_by('pub_date')
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)