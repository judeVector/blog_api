from django.urls import path

from .views import *

urlpatterns = [
    path("status/", get_status, name="status"),
    path("posts/", post_list, name="posts"),
]
