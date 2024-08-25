from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def get_status(request: Request):
    data = {"status": "Server is working"}
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def post_list(request: Request):
    if request.method == "GET":
        data = Post.objects.all()
        serializer_data = PostSerializer(data, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        try:
            post = Post.objects.create(
                title=request.data["title"], post=request.data["post"]
            )
            serializer_data = PostSerializer(post, many=False)
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
