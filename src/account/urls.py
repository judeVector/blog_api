from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import *

urlpatterns = [
    path("auth/signup/", SignUpView.as_view(), name="signup"),
    path("auth/signin/", LoginView.as_view(), name="signin"),
    path("auth/regenerate/", RegenerateTokenView.as_view(), name="regenerate"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
]
