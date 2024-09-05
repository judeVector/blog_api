from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class PostListCreateViewTestCase(APITestCase):

    def setUp(self):
        self.post_url = reverse("posts")
        self.signup_url = reverse("signup")
        self.login_url = reverse("signin")

    def authenticate(self):
        user = {
            "username": "johndoe",
            "email": "johndoe@email.com",
            "password": "password1234",
        }
        self.client.post(self.signup_url, user)
        response = self.client.post(
            self.login_url,
            {
                "email": "johndoe@email.com",
                "password": "password1234",
            },
        )
        token = response.data["data"]["token"]["access_token"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_list_posts(self):
        self.authenticate()
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"]["data"], [])

    def test_create_post(self):
        self.authenticate()
        response = self.client.post(
            self.post_url,
            {
                "title": "Sample Post",
                "content": "This is a sample post.",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["data"]["title"], "Sample Post")
