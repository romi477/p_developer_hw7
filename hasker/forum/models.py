from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    avatar = models.FileField(upload_to='static/avatars/')

    def __str__(self):
        return f'<{self.username}: {self.email}>'

    def get_absolute_url(self):
        return reverse('personal_info', {'name': self.username})




