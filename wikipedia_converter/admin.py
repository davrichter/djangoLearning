from django.contrib import admin

from .models import Article, FullArticle, User

admin.site.register(Article)
admin.site.register(FullArticle)
admin.site.register(User)
