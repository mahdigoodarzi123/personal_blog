from django.db import models
import datetime
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    post = models.TextField()
    # post = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return self.title
    