from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import DeleteOwnPost

# Create your views here.


class PostListCreateView(CreateAPIView):
    """
    A view creating post by authenticated users

    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveDestroyView(RetrieveDestroyAPIView):
    """
    A view for retrieving post by id and deleting post by id

    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DeleteOwnPost]
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": f"{instance.title.title()} deleted successfully."})


class PostLikeView(APIView):
    """
    A view for liking a post requires users to be authenticated and postID

    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, id):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        user = request.user
        if post.has_user_liked(user):
            return Response(
                {"detail": "You have already liked this post"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        post.likes.add(request.user)
        return Response({"detail": "Post liked successfully."})


class PostUnlikeView(APIView):
    """
    A view for unliking a post requires users to be authenticated and postID

    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, id):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        user = request.user

        if not post.has_user_liked(user):
            return Response(
                {"detail": "You have not liked this post yet"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        post.likes.remove(request.user)
        return Response({"detail": "Post unLiked successfully."})


class PostListByUserAPIView(ListAPIView):
    """
    A view for retrieving all the post created by authenticated users

    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user).order_by("-created_at")


class CommentCreateAPIView(CreateAPIView):
    """
    A view for adding comments on the post, requires user's to be authenticated and postID

    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs.get("id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(post=post, user=self.request.user)
