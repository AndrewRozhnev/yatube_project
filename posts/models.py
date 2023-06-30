from django.contrib.auth import get_user_model
from django.db import models
from pytils.translit import slugify


class Group(models.Model):
    title = models.CharField(max_length=20, help_text='Enter a group title')
    slug = models.SlugField(
        unique=True,
        blank=True,
        help_text='Generated automatically from the group title'
    )
    description = models.TextField(help_text='Enter a description of the group')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    text = models.TextField(verbose_name='post description', help_text='Enter the post text')
    pub_date = models.DateTimeField(
        verbose_name='date of publication',
        auto_now_add=True,
        help_text='Generated automatically when the post is published'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Choose the author of the post'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        help_text='Select the group to which the post belongs'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.text[:20]
