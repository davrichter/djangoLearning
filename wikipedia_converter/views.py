from django.template import loader
from django.views import generic
from django.http import HttpResponse

import wikipedia

from .models import Article
from .article_converter import article_convert


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'wikipedia_converter/index.html'
    context_object_name = 'old_articles'

    def get_queryset(self):
        return Article.objects.all()


def article(request):
    article_original = wikipedia.page(request.POST['title'])

    article_text_formatted = article_convert(article_original.content)

    template = loader.get_template('wikipedia_converter/article.html')

    # use the formatted text but for title, link, ... the standard WikipediaPage object
    context = {
        'article': article_original,
        'article_text_formatted': article_text_formatted,
    }

    return HttpResponse(template.render(context, request))


def get_articles(request):
    language = request.POST['language']
    wikipedia.set_lang(language)

    search = request.POST['search']

    # if searching for empty string dont search for it on wikipedia
    # that will return an error just assign it to an empty array
    if search != "":
        search_results = wikipedia.search(search)
    else:
        search_results = []

    template = loader.get_template('wikipedia_converter/search_results.html')

    context = {
        'search': search,
        'search_results': search_results,
    }

    return HttpResponse(template.render(context, request))
