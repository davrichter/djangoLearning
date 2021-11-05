from django.shortcuts import render
from django.views import generic

from .models import Article

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'wikipedia_converter/index.html'
    context_object_name = 'old_articles'

    def get_queryset(self):
        return Article.objects.all()
    