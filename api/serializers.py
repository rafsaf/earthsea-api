import re

from rest_framework import serializers

import api.models as models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ["id", "confirmed", "main_page", "title", "slug", "category",
                  "description", "author", "created", "image", "image_confirm", "source", "like", ]

    def validate_title(self, value):
        pattern = "^[\sAaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrQqSsŚśTtUuWwYyZzŹźŻż:();/.,!'\"?!/]+$"
        if len(value) < 3:
            raise serializers.ValidationError("Tekst nie może być krótszy niż 3 znaki.")
        if len(value) > 24:
            raise serializers.ValidationError("Tekst nie może być dłuższy niż 24 znaków.")

        result = re.match(pattern=pattern, string=value)
        if not result:
            raise serializers.ValidationError(
                "Dozwolone tylko małe, duże litery, podstawowe znaki interpunkcyjne.")
        return value

    def validate_slug(self, value):
        pattern = "^[a-z](-?[a-z])*$"
        if len(value) < 3:
            raise serializers.ValidationError("Tekst nie może być krótszy niż 3 znaki.")
        if len(value) > 100:
            raise serializers.ValidationError("Tekst nie może być dłuższy niż 100 znaków.")
        
        result = re.match(pattern=pattern, string=value)
        if not result:
            raise serializers.ValidationError(
                "Dozwolone tylko [a-z]-[a-z]-[...] itd. Na przykład „czarnoksieznik-z-archipelagu”.")
        return value

    def validate_author(self, value):
        pattern = "^[\sAaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrQqSsŚśTtUuWwYyZzŹźŻż:();/.,!'\"?!/]+$"
        if len(value) < 3:
            raise serializers.ValidationError("Tekst nie może być krótszy niż 3 znaki.")
        if len(value) > 24:
            raise serializers.ValidationError("Tekst nie może być dłuższy niż 24 znaków.")

        result = re.match(pattern=pattern, string=value)
        if not result:
            raise serializers.ValidationError(
                "Dozwolone tylko małe, duże litery, podstawowe znaki interpunkcyjne.")
        return value

    def validate_description(self, value):
        pattern = "^[\sAaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrQqSsŚśTtUuWwYyZzŹźŻż:();/.,!'\"?!/]+$"
        if len(value) < 50:
            raise serializers.ValidationError("Tekst nie może być krótszy niż 50 znaków.")
        if len(value) > 160:
            raise serializers.ValidationError("Tekst nie może być dłuższy niż 160 znaków.")

        result = re.match(pattern=pattern, string=value)
        if not result:
            raise serializers.ValidationError(
                "Dozwolone tylko małe, duże litery, podstawowe znaki interpunkcyjne.")
        return value


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = ["id", "article", "created", "text", "confirm"]
