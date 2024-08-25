from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def server_detail(request: Request):
    response = {
        "name": "Blog API",
        "version": "1.0.0",
        "author": "Jude Ndubuisi",
        "contact": "ikechukwujudendubuisi@gmail.com",
        "website": "https://judevector.dev",
        "description": "A simple REST API for managing blog posts",
        "twitter": "http://twitter.com/judevector",
    }

    return Response(data=response, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_status(request: Request):
    data = {"status": "Server is working"}
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def get_or_create_post(request: Request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer_data = PostSerializer(posts, many=True)

        response = {
            "message": "posts",
            "data": serializer_data.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer_data = PostSerializer(data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            response = {
                "message": "Post created successfully",
                "data": serializer_data.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def get_update_delete_by_id(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "GET":
        serializer_data = PostSerializer(instance=post)
        response = {
            "message": "post",
            "data": serializer_data.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer_data = PostSerializer(instance=post, data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            response = {
                "message": "Post updated successfully",
                "data": serializer_data.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        post.delete()
        response = {"message": "Post deleted successfully"}
        return Response(response, status=status.HTTP_200_OK)
