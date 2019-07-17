from rest_framework import serializers
from django.apps import apps


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = apps.get_model('authorization', 'Person')
        fields = ['username', 'email', 'avatar', 'date_joined']


class QuestionSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = apps.get_model('forum', 'Question')
        fields = ['title', 'content', 'author', 'pub_date']
        
        
class ReplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = apps.get_model('forum', 'Reply')
        fields = ['related_q', 'body', 'author', 'pub_date']