from django.urls import path

from .views import *

urlpatterns = [
    path("detail/", server_detail, name="server_detail"),
    path("status/", get_status, name="status"),
    path("posts/", get_or_create_post, name="posts"),
    path("posts/<int:post_id>", get_update_delete_by_id, name="posts"),
]
