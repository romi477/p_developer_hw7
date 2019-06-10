from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class Person(AbstractUser):

    class Meta:
        verbose_name = 'Person'


class PersonProfile(models.Model):
    person = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __str__(self):
        return f'{self.person.username} <{self.person.email}>'
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_person_profile(sender, instance, **kwargs):
    if kwargs['created']:
        PersonProfile.objects.create(person=instance)
    instance.profile.save()

# post_save.connect(create_person_profile, sender=settings.AUTH_USER_MODEL)


class Test(models.Model):
    person = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __str__(self):
        return self.person

