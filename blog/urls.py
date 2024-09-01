from django.urls import path

from .views import *

urlpatterns = [
    path("homepage/", homepage, name="homepage"),
    path("detail/", ServerDetailView.as_view(), name="server_detail"),
    path("status/", ServerStatusView.as_view(), name="status"),
    path("posts/", PostListCreateView.as_view(), name="posts"),
    path(
        "posts/<int:post_id>", PostRetrieveUpdateDeleteView.as_view(), name="postbyid"
    ),
]
