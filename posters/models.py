from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published_date = models.DateField(auto_now=True)
    body = models.CharField(max_length=2000)

    def get_absolute_url(self):
        return reverse("posters:detail", kwargs={"id": self.pk})
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
    author = models.CharField(max_length=50)
    published_date = models.DateField(auto_now=True)
    body_text = models.CharField(max_length=250,default="empty")