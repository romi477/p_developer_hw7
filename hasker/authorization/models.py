from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser



class Person(AbstractUser):
    
    class Meta:
        verbose_name = 'Person'
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('user_profile', {'nick': self.username})


class UserProfile(models.Model):
    user = models.OneToOneField(Person, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __repr__(self):
        return self.user


@receiver(post_save, sender=Person)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=Person)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Test(models.Model):
    person = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __repr__(self):
        return self.person

