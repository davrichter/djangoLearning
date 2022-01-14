from django.urls import path

from . import views

app_name: str = 'wikipedia_converter'
urlpatterns = [
    path('', views.index, name="Index"),
    path('search', views.get_articles, name="getArticles"),
    path('article', views.article, name="article"),
    path('article/save', views.save_article, name="saveArticle"),
    path('article/db/get/<int:pk>', views.get_article_from_db, name="getArticleFromDb"),
    path('article/db/delete/<int:pk>', views.delete_article_from_db, name="deleteArticleFromDb"),
    path('privacy', views.privacy, name="privacy"),
    path('about', views.about, name="about"),
    path('change-theme', views.change_theme, name="changeTheme")
]
