from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse
from .utils import unique_slug_generator
from django.core.mail import send_mail


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
    title = models.CharField(max_length=255, db_index=True, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=144, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='questions')
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return f'{self.title[:11]} - {self.author}'
    
    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'slug': self.slug})
    
    def save(self, tag_list=[], *args, **kwargs):
        if not self.id:
            self.slug = unique_slug_generator(self, self.title)
        super(Question, self).save(*args, **kwargs)
        tags = []
        for t in tag_list:
            tag, created = Tag.objects.get_or_create(name=t)
            tags.append(tag)
            self.tags.add(*tags)

    @property
    def total_votes(self):
        return self.votes.count()
    

class Reply(models.Model):
    related_q = models.ForeignKey(Question, related_name='replies', on_delete=models.CASCADE)
    body = models.TextField(db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    flag = models.BooleanField(default=False)
    votes = GenericRelation(Vote)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return f'{self.body[:14]} - {self.author}'

    def send_email(self, mail_body):
        send_mail(
            'Hasker notification',
            mail_body,
            settings.EMAIL_HOST_USER,
            [self.related_q.author.email]
        )
    
    @property
    def total_votes(self):
        return self.votes.count()