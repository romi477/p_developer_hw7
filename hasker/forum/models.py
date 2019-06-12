from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Tag(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=25, unique=True)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=144, db_index=True)
    content = models.TextField()
    slug = models.SlugField(max_length=72, unique=True)
    creation = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, null=True, related_name='questions')
    
    def __str__(self):
        return f'{self.title[:11]} - {self.author}'
    
    
class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation = models.DateField(auto_now_add=True)
    flag = models.NullBooleanField()
    votes = GenericRelation(Vote)
    
    def __str__(self):
        return f'{self.content[:14]} - {self.author}'
    