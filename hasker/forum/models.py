from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from django.shortcuts import reverse


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Tag(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=144, db_index=True)
    content = models.TextField()
    slug = models.SlugField(max_length=72, unique=True)
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='questions')

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return f'{self.title[:11]} - {self.author}'
    
    def get_absolure_url(self):
        return reverse('question_detail', {'slug': self.slug})
    
    def save(self, tag_list=[], *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)
        tags = []
        for t in tag_list:
            tag, created = Tag.objects.get_or_create(name=t)
            tags.append(tag)
            self.tags.add(*tags)
    

class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    flag = models.NullBooleanField()
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ('-pub_date',)
    
    def __str__(self):
        return f'{self.content[:14]} - {self.author}'
