from django.db import models

from django.contrib.auth.models import User
# Create your models here.
import datetime as dt
from tinymce.models import HTMLField


class Profile(models.Model):
    bio=models.TextField(max_length=100,blank=True,default="bio please...")
    profilepic=models.ImageField(upload_to='profile/', blank = True,default='../static/images/bad-profile-pic-2.jpeg')
    email=models.CharField(blank=True,max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user