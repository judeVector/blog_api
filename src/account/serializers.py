from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used.")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    raise AuthenticationFailed("Account is disabled.")

                # Attach the token to the user or create it if it doesn't exist
                token, created = Token.objects.get_or_create(user=user)
                attrs["user"] = user
                attrs["token"] = token.key
            else:
                raise AuthenticationFailed("Invalid email or password.")
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        return attrs


class RegenerateTokenSerializer(serializers.Serializer):
    def save(self, user):
        # Delete the old token
        Token.objects.filter(user=user).delete()
        # Create a new token
        new_token = Token.objects.create(user=user)
        return new_token.key
