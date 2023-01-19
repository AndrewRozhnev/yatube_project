from django.contrib.auth import get_user_model
from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='posts')
    group = models.ForeignKey(Group,
                              on_delete=models.CASCADE,
                              related_name='posts',
                              blank=True,
                              null=True)

    def __str__(self):
        return self.text
