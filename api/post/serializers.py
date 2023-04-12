from rest_framework import serializers
from .models import Post
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "user", "text", "created_at", "updated_at"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "description",
            "author",
            "comments",
            "total_likes",
            "created_at",
            "updated_at",
        ]
