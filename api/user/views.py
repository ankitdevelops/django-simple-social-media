from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class FollowUserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, userId, *args, **kwargs):
        try:
            user_to_follow = User.objects.get(pk=userId)
        except User.DoesNotExist:
            return Response(
                {"detail": "User Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if request.user == user_to_follow:
            return Response(
                {"detail": "You can't follow/unfollow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if request.user.is_following(user_to_follow):
            return Response(
                f"{request.user.username} is Already Following {user_to_follow.username}",
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.user.follow(user_to_follow)

        return Response(
            {
                "detail": f"{request.user.username} Started Following {user_to_follow.username}"
            },
            status=status.HTTP_200_OK,
        )


class UnFollowUserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, userId, *args, **kwargs):
        try:
            user_to_unfollow = User.objects.get(pk=userId)
        except User.DoesNotExist:
            return Response(
                {"detail": "User Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if request.user == user_to_unfollow:
            return Response(
                {"detail": "You can't follow/unfollow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not request.user.is_following(user_to_unfollow):
            return Response(
                f"{request.user.username} is Not Following {user_to_unfollow.username}",
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.user.unfollow(user_to_unfollow)

        return Response(
            {
                "detail": f"{request.user.username} Stopped Following {user_to_unfollow.username}"
            },
            status=status.HTTP_200_OK,
        )
