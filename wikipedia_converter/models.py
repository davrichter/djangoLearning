from django.db import models
import wikipedia

# Create your models here.

class Article(models.Model):
    page = wikipedia.WikipediaPage
    original_page = wikipedia.WikipediaPage
    receiving_date = models.DateTimeField('date pulled from wikipedia')
