from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    post = models.TextField(max_length=280, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
