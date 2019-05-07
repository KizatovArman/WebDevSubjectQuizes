from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class PostManager(models.Manager):
    def for_user(self,user):
        return self.filter(created_by=user)

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=400)
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    objects = PostManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

    def to_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'like_count': self.like_count,
            'created_at': self.created_at,
        }

