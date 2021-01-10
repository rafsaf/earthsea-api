from django.contrib import admin

import api.models as models


admin.site.register(models.Article) 
admin.site.register(models.Version) 