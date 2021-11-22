from django.urls import path

from . import views

app_name: str = 'wikipedia_converter'
urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('search', views.get_articles, name="getArticles"),
    path('article', views.article, name="article"),
    path('article/save', views.save_article, name="saveArticle")
]
