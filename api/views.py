from django.http import Http404, response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from api.models import Article, Version
from api.serializers import ArticleSerializer, VersionSerializer


class ArticleList(APIView):
    """
    List of all articles, if GET main_page=true, only home page articles
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        main_page = request.GET.get("main_page")
        latest = request.GET.get("latest")
        if main_page == "true":
            articles = articles.filter(main_page=True, confirmed=True, image_confirm=True)
        if latest == "true":
            articles = articles.filter(confirmed=True).exclude(main_page=True).order_by("-created_time")[:5]
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetail(APIView):
    """
    Retreive, create, update article
    """
    def get(self, request, slug, format=None):
        article = get_object_or_404(Article, slug=slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleLike(APIView):
    """
    Like an article
    """
    def post(self, request, slug, format=None):
        article = get_object_or_404(Article, slug=slug)
        data = {"like": article.like + 1}
        serializer = ArticleSerializer(article, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ArticleVersion(APIView):
    """
    Retreive all versions for given article
    """

    def get(self, request, slug, format=None):
        article = get_object_or_404(Article, slug=slug)
        versions = Version.objects.filter(article=article)
        serializer = VersionSerializer(versions, many=True)

        return Response(serializer.data)

class VersionDetail(APIView):
    """
    Single version 
    """
    def post(self, request, format=None):
        slug = request.data.get("slug")
        article = get_object_or_404(Article, slug=slug)
        text = request.data.get("text")
        new_version = VersionSerializer(data={"article": article.id, "text": text}, partial=True)
        if new_version.is_valid():
            new_version.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
