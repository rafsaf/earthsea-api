from rest_framework import serializers

import api.models as models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ["id", "confirmed", "main_page", "title", "slug", "category", "description","author", "created", "image", "image_confirm", "source", "like",]
        optional_fields = ["image", "source", "like", "created", ]


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = ["id", "article", "created", "text", "confirm"]
