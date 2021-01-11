from api.models import Version
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import api.views as views


urlpatterns = [
    path("articles/", views.ArticleList.as_view(), name="article_list"),
    path("article/<str:slug>/", views.ArticleDetail.as_view(), name="article_detail"),
    path("article/<str:slug>/like", views.ArticleLike.as_view(), name="article_like"),
    path("article/version/<str:slug>/", views.ArticleVersion.as_view(), name="article_version"),
    path("version/", views.VersionDetail.as_view(), name="version_detail"),
]
