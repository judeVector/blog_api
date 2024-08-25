from rest_framework.serializers import ModelSerializer

from .views import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "post"]
