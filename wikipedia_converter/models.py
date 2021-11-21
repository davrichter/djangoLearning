from django.db import models


# Create your models here.

class Article(models.Model):
    content = models.CharField
    link = models.CharField
    title = models.CharField

    def __str__(self):
        return self.content


class FullArticle(models.Model):
    page = Article
    original_page = Article
    date_pulled = models.DateTimeField('date pulled from wikipedia')

    def __str__(self):
        return f"{self.page.title}: {self.date_pulled}"
