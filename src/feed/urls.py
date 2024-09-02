from django.urls import path

from .views import *

urlpatterns = [
    path("feeds/", ListPostsForAuthor.as_view(), name="user_posts"),
]
