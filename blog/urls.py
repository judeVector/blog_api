from django.urls import path

from .views import *

urlpatterns = [
    path("detail/", ServerDetail.as_view(), name="server_detail"),
    path("status/", ServerStatus.as_view(), name="status"),
    path("posts/", GetOrCreatePost.as_view(), name="posts"),
    path("posts/<int:post_id>", GetUpdateOrDeleteById.as_view(), name="posts"),
]
