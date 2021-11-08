from django.urls import path

from . import views

app_name: str = 'wikipedia_converter'
urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('str:search', views.get_articles, name="getArticles")
]
