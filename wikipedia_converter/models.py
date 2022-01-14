from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    text_theme = models.CharField(max_length=5)
    bg_theme = models.CharField(max_length=5)


class Article(models.Model):
    content = models.CharField(max_length=9999999999)
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class FullArticle(models.Model):
    formatted_page = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="formatted_page")
    original_page = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_pulled = models.DateTimeField('date pulled from wikipedia')

    def __str__(self):
        return self.formatted_page.title
