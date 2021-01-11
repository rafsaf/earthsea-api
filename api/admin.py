from django.contrib import admin

import api.models as models

@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ["article", "created", "confirm", "text" ]
    list_editable = ["confirm" ]

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "confirmed", "created" ]
    list_editable = ["confirmed" ]