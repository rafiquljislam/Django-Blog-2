from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    commentsss = models.TextField()
    def __str__(self):
        return self.fname
