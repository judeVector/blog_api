from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post objects"""

    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "post",
            "created_at",
            "updated_at",
            "author_id",
            "author_username",
        ]

    def get_author_username(self, obj) -> str:
        return obj.author.username if obj.author else None

    def to_representation(self, instance):
        # This replaces the "author_username" field with just "author"
        representation = super().to_representation(instance)
        representation["author"] = representation.pop("author_username")
        return representation


class ServerDetailSerializer(serializers.Serializer):
    name = serializers.CharField(default="Blog API")
    version = serializers.CharField(default="1.0.0")
    author = serializers.CharField(default="Jude Ndubuisi")
    contact = serializers.EmailField(default="ikechukwujudendubuisi@gmail.com")
    website = serializers.URLField(default="https://judevector.vercel.app")
    description = serializers.CharField(
        default="A simple REST API for managing blog posts"
    )
    twitter = serializers.URLField(default="https://twitter.com/judevector")
    github = serializers.URLField(default="https://github.com/judevector")


class ServerStatusSerializer(serializers.Serializer):
    message = serializers.CharField(default="success")
    status = serializers.CharField()
