from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class Person(AbstractUser):

    class Meta:
        verbose_name = 'Person'

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('person_profile', {'nick': self.username})


class PersonalProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __repr__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_personal_profile(sender, **kwargs):
    if kwargs['created']:
        PersonalProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_personal_profile, sender=settings.AUTH_USER_MODEL)


class Test(models.Model):
    person = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/def_ava.jpg')

    def __str__(self):
        return self.person

