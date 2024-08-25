from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    post = models.TextField(max_length=280, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
