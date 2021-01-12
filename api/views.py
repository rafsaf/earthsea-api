from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Article, Version, DailySimpleHit
from api.serializers import ArticleSerializer, VersionSerializer


def add_simple_hit(field):
    today_hits = DailySimpleHit.objects.get_or_create(date=timezone.now(), defaults={"date": timezone.now()})[0]
    if field == "home":
        today_hits.home_hits += 1
    elif field == "category":
        today_hits.category_hits += 1
    elif field == "article":
        today_hits.article_hits += 1
    today_hits.save()


class ArticleList(APIView):
    """
    GET List of all articles, if GET main_page=true, only home page articles.
    POST to create new article.
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        main_page = request.GET.get("main_page")
        latest = request.GET.get("latest")
        if main_page == "true":
            articles = articles.filter(main_page=True, confirmed=True, image_confirm=True)
            add_simple_hit("home")
        elif latest == "true":
            articles = articles.filter(confirmed=True).exclude(main_page=True).order_by("-created_time")[:5]
        else:
            add_simple_hit("category")

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        new_article = ArticleSerializer(data=request.data, partial=True)
        if new_article.is_valid():
            new_article.save()
            return Response(new_article.data, status=status.HTTP_201_CREATED)
        return Response(new_article.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    """
    Retreive, create, update article
    """
    def get(self, request, slug, format=None):
        article = get_object_or_404(Article, slug=slug)
        article.views += 1
        article.save()
        add_simple_hit("article")
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleLike(APIView):
    """
    Like +1 for given article
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
        versions = Version.objects.filter(article=article, archived=False)
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
