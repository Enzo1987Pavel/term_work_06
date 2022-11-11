from rest_framework import serializers

from ads.models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name")
    # author_last_name = serializers.CharField(sources="author.last_name")
    # author_id = serializers.CharField(sources="author.id")

    class Meta:
        model = Ad
        fields = "__all__"


# class CommentSerializer(serializers.ModelSerializer):
#     author_first_name = serializers.CharField(max_length=50, read_only=True)
#     author_last_name = serializers.CharField(max_length=50, read_only=True)
#     author_image = serializers.ImageField(read_only=True)
#
#     class Meta:
#         model = Comment
#         fields = [
#             "pk",
#             "text",
#             "author_id",
#             "create_at",
#             "author_first_name",
#             "author_last_name",
#             "ad_id",
#             "author_image",
#         ]

    def get_fields(self):
        data = getattr(self, "instance", None)

        if isinstance(data, list):
            for obj in data:
                author = getattr(obj, "author", None)

                obj.author_first_name = author.first_name
                obj.author_last_name = author.last_name
                obj.author_image = author.image

        elif data:
            author = getattr(data, "author", None)

            self.instance.author_first_name = author.first_name
            self.instance.author_last_name = author.last_name
            self.instance.author_image = author.image
