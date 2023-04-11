from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from .models import Post

user = get_user_model()


class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = user.objects.create_user(
            username="testuser",
            password="testpass123",
            email="testuser@gmail.com",
            name="Test User",
        )
        self.access_token = AccessToken.for_user(self.user)

    def test_create_post(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.access_token))

        post_data = {
            "title": "Test Post",
            "description": "This is a test post.",
        }

        response = self.client.post("/api/posts/", post_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "Test Post")
        self.assertEqual(Post.objects.get().description, "This is a test post.")
        self.assertEqual(Post.objects.get().author, self.user)

    def tearDown(self):
        self.user.delete()
