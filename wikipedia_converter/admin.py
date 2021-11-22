from django.contrib import admin

from .models import Article, FullArticle

admin.site.register(Article)
admin.site.register(FullArticle)
