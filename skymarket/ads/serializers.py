from rest_framework import serializers

from ads.models import Ad


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass
