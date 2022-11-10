from rest_framework import serializers

from ads.models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=50, read_only=True)
    author_last_name = serializers.CharField(max_length=50, read_only=True)
    author_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "create_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image",
        ]
