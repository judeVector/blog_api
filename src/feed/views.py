from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from blog.models import Post
from blog.serializers import PostSerializer

tags = ["Feed"]


class ListPostsForAuthor(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    @extend_schema(
        operation_id="list_posts_by_author",
        summary="List Posts by Author",
        description="This endpoint filters and list all posts created by users",
        tags=tags,
        parameters=[
            OpenApiParameter(
                name="username",
                description="Optional. Filters by author's username; defaults to all posts if not provided.",
                required=False,
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    def get(self, request: Request, *args, **kwargs):
        username = self.request.query_params.get("username") or None
        # pagination
        paginator = PageNumberPagination()

        if username is not None:
            queryset = self.get_queryset().filter(author__username=username)
            serializer_data = self.get_serializer(queryset, many=True)

            response = {
                "message": f"{username}'s posts",
                "data": serializer_data.data,
            }

            return Response(data=response, status=status.HTTP_200_OK)

        paginated_posts = paginator.paginate_queryset(self.get_queryset(), request)
        serializer_data = self.get_serializer(instance=paginated_posts, many=True)

        # serializer_data = self.get_serializer(self.get_queryset(), many=True)
        response = {
            "message": "All posts",
            "data": serializer_data.data,
        }

        return paginator.get_paginated_response(response)
        # return Response(data=response, status=status.HTTP_200_OK)
