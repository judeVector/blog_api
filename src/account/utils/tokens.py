from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken


def create_jwt_pair_for_user(user: User):
    refresh_token = RefreshToken.for_user(user)

    tokens = {
        "access_token": str(refresh_token.access_token),
        "refresh_token": str(refresh_token),
    }
    return tokens
