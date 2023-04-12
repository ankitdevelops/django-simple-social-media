from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import MyAccountManager


class MyAccountManagerTest(TestCase):
    def test_create_user(self):
        user = get_user_model()
        email = "testuser@test.com"
        password = "testpass123"
        username = "testuser"
        name = "testuser"
        user = user.objects.create_user(
            email=email, password=password, username=username, name=name
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        user = get_user_model()
        email = "admin@test.com"
        password = "adminpass123"
        username = "admin"
        name = "admin"
        user = user.objects.create_superuser(
            email=email, password=password, username=username, name=name
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class UserModelTest(TestCase):
    def test_follow(self):
        User = get_user_model()
        user1 = User.objects.create_user(
            email="testuser1@test.com",
            password="testpass123",
            username="testuser1",
            name="testuser1",
        )
        user2 = User.objects.create_user(
            email="testuser2@test.com",
            password="testpass456",
            username="testuser2",
            name="testuser2",
        )
        user1.follow(user2)
        self.assertTrue(user1.is_following(user2))
        self.assertFalse(user2.is_following(user1))

    def test_unfollow(self):
        User = get_user_model()
        user1 = User.objects.create_user(
            email="testuser3@test.com",
            password="testpass123",
            username="testuser3",
            name="testuser3",
        )
        user2 = User.objects.create_user(
            email="testuser4@test.com",
            password="testpass456",
            username="testuser4",
            name="testuser1",
        )
        user1.follow(user2)
        user1.unfollow(user2)
        self.assertFalse(user1.is_following(user2))

    def test_is_following(self):
        User = get_user_model()
        user1 = User.objects.create_user(
            email="testuser5@test.com",
            password="testpass123",
            username="testuser5",
            name="testuser1",
        )
        user2 = User.objects.create_user(
            email="testuser6@test.com",
            password="testpass456",
            username="testuser6",
            name="testuser1",
        )
        user1.follow(user2)
        self.assertTrue(user1.is_following(user2))
        self.assertFalse(user2.is_following(user1))
