from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)

    class Meta:
        model = Post
        fields = ["id", "title", "post", "created_at", "updated_at"]


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
