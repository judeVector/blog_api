from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import SignUpSerializer

from drf_spectacular.utils import extend_schema

# Create your views here.

tags = ["Auth"]


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    @extend_schema(
        summary="Register a new user",
        description="This endpoint registers a new user",
        tags=tags,
    )
    def post(self, request: Request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            response = {
                "message": "User created successfully",
                "data": serializer_data.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
