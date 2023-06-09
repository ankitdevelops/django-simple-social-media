from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.user.views import (
    FollowUserView,
    UnFollowUserView,
    UserProfileView,
)
from api.post.views import (
    PostListCreateView,
    PostRetrieveDestroyView,
    PostLikeView,
    PostUnlikeView,
    PostListByUserAPIView,
    CommentCreateAPIView,
)

urlpatterns = [
    # user app related routes
    path("authenticate/", TokenObtainPairView.as_view()),
    path("user/", UserProfileView.as_view()),
    path("follow/<int:userId>/", FollowUserView.as_view()),
    path("unfollow/<int:userId>/", UnFollowUserView.as_view()),
    # post app related routes
    path("posts/", PostListCreateView.as_view(), name="add_post"),
    path("posts/<int:id>/", PostRetrieveDestroyView.as_view()),
    path("like/<int:id>/", PostLikeView.as_view()),
    path("unlike/<int:id>/", PostUnlikeView.as_view()),
    path("all_posts/", PostListByUserAPIView.as_view()),
    path("comment/<int:id>/", CommentCreateAPIView.as_view()),
]
