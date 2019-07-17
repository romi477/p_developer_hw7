from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    
    class Meta:
        verbose_name = 'Person'

    email = models.EmailField(max_length=254, unique=True, verbose_name='email address')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __str__(self):
        return f'{self.username} <{self.email}>'

