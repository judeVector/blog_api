from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

from drf_spectacular.utils import extend_schema

from .models import Post
from .serializers import PostSerializer, ServerDetailSerializer, ServerStatusSerializer
from .permissions import AuthorOrReadOnlyPermission

tags = ["Post"]


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data

        response = {"message": "Hello World", "data": data}

        return Response(data=response, status=status.HTTP_200_OK)
    response = {"message": "Hello World"}

    return Response(data=response, status=status.HTTP_200_OK)


class ServerDetailView(APIView):
    serializer_class = ServerDetailSerializer

    @extend_schema(
        summary="Retrieve site details",
        description="This endpoint retrieves a few details of the site/application",
        tags=["Server Details"],
    )
    def get(self, request: Request):
        response = {
            "name": "Blog API",
            "version": "1.0.0",
            "author": "Jude Ndubuisi",
            "contact": "ikechukwujudendubuisi@gmail.com",
            "website": "https://judevector.vercel.app/",
            "description": "A simple REST API for managing blog posts",
            "twitter": "https://twitter.com/judevector",
            "github": "https://github.com/judevector",
        }
        return Response(data=response, status=status.HTTP_200_OK)


class ServerStatusView(APIView):
    serializer_class = ServerStatusSerializer

    @extend_schema(
        summary="API health check",
        description="This endpoint checks the health of the API",
        tags=["HealthCheck"],
    )
    def get(self, request: Request):
        response = {"message": "success", "status": "Server is working properly"}
        return Response(data=response, status=status.HTTP_200_OK)


class PostListCreateView(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        operation_id="list_posts",
        summary="Retrieve Posts",
        description="This endpoint retrieves a list of posts",
        tags=tags,
    )
    def get(self, request: Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer_data = self.serializer_class(instance=posts, many=True)
        response = {
            "message": "posts",
            "data": serializer_data.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create Post",
        description="This endpoint creates a new post",
        tags=tags,
    )
    def post(self, request: Request):
        serializer_data = self.serializer_class(data=request.data)

        if serializer_data.is_valid():
            serializer_data.save(author=request.user)  # Assign the author
            response = {
                "message": "Post created successfully",
                "data": serializer_data.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnlyPermission]

    def get(self, request: Request, post_id: int):
        post = get_object_or_404(Post, pk=post_id)
        self.check_object_permissions(request, post)
        serializer_data = self.serializer_class(instance=post)

        response = {
            "message": "post",
            "data": serializer_data.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request: Request, post_id: int):
        post = get_object_or_404(Post, pk=post_id)
        self.check_object_permissions(request, post)
        serializer_data = self.serializer_class(instance=post, data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            response = {
                "message": "Post updated successfully",
                "data": serializer_data.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, post_id: int):
        post = get_object_or_404(Post, pk=post_id)
        self.check_object_permissions(request, post)
        post.delete()
        response = {"message": "Post deleted successfully"}
        return Response(response, status=status.HTTP_200_OK)
