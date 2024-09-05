from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from .views import PostListCreateView

User = get_user_model()


class PostListCreateViewTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PostListCreateView.as_view()
        self.url = reverse("posts")
        self.user = User.objects.create(
            username="judevector", email="vector@email.com", password="password1234"
        )

    # def test_list_posts(self):
    #     request = self.factory.get(self.url)
    #     response = self.view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        sample_post = {"title": "Sample Post", "content": "This is a sample post."}
        request = self.factory.post(self.url, sample_post)
        request.user = self.user
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
