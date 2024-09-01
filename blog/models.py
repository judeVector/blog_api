from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    post = models.TextField(max_length=280, blank=False, null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
