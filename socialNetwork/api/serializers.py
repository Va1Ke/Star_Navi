from rest_framework import serializers
from socialNetwork.models import Post, Like, User


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.StringRelatedField()
    last_time_request = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ["last_login", "last_time_request"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    likes_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ["id", "author", "title", "body", "created_at", "likes_count"]


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    content_type = serializers.SerializerMethodField()
    object_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ["user", "created_at", "content_type", "object_id"]

    def get_content_type(self, obj):
        return obj.content_type.model
