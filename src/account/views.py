from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_spectacular.utils import extend_schema

from .serializers import SignUpSerializer, LoginSerializer, RegenerateTokenSerializer
from .utils.tokens import create_jwt_pair_for_user


# Create your views here.

tags = ["Auth"]


class SignUpView(generics.GenericAPIView):
    permission_classes = [AllowAny]
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


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @extend_schema(
        summary="Login a user",
        description="This endpoint logs in a user",
        tags=tags,
    )
    def post(self, request: Request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)

        user = serializer_data.validated_data["user"]
        # token = serializer_data.validated_data["token"]
        tokens = create_jwt_pair_for_user(user)

        response = {
            "message": "User logged in successfully",
            "data": {"token": tokens},
        }
        return Response(data=response, status=status.HTTP_200_OK)


class RegenerateTokenView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegenerateTokenSerializer

    @extend_schema(
        summary="Regenerate API Token",
        description="This endpoint regenerates the user's API token",
        tags=tags,
    )
    def post(self, request, *args, **kwargs):
        new_token_key = self.serializer_class().save(user=request.user)

        return Response(
            {"message": "API token regenerated successfully", "token": new_token_key},
            status=status.HTTP_200_OK,
        )
