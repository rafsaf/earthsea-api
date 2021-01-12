from django.contrib import admin

import api.models as models

@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ["article", "created", "confirm", "archived", "text" ]
    list_editable = ["confirm" , "archived"]
    readonly_fields = ["article", "created", "text"]

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "confirmed", "main_page", "image_confirm", "created", "views" ]
    list_editable = ["confirmed" , "main_page", "image_confirm"]
    readonly_fields = ["title", "slug", "created", "views", "like", "author", "description", "category",]

@admin.register(models.DailySimpleHit)
class DailyHitsAdmin(admin.ModelAdmin):
    list_display = ["date", "home_hits", "category_hits", "article_hits"]
    readonly_fields = ["date", "home_hits", "category_hits", "article_hits"]