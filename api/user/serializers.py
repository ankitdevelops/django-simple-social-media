from rest_framework import serializers
from .models import User


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class UserSerializer(serializers.ModelSerializer):
    following = FollowingSerializer(many=True, read_only=True)
    followers = FollowingSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "email",
            "phone_number",
            "joined",
            "last_login",
            "following",
            "followers",
        ]
