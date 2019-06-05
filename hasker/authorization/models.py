from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars')
    
    def __repr__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


class Test(models.Model):
    person = models.CharField(max_length=10)
    # avatar = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatars', default='avatars/def_ava.jpg')
    
    def __repr__(self):
        return self.person
    
    