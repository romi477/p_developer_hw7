from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings




class Person(AbstractUser):
    
    class Meta:
        verbose_name = 'Person'

    email = models.EmailField(max_length=254, unique=True, verbose_name='email address')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __str__(self):
        return f'{self.username} <{self.email}>'

   

class Test(models.Model):
    person = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __str__(self):
        return self.person

