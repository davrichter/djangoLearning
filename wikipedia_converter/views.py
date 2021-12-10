from django.template import loader
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

import wikipedia

from .models import Article, FullArticle
from .article_converter import article_convert


# base django views:

def index(request):
    template = loader.get_template('wikipedia_converter/index.html')
    articles = list(FullArticle.objects.all())

    context = {
        'articles': articles,
    }

    return HttpResponse(template.render(context, request))


def article(request):
    try:
        article_original = wikipedia.page(request.POST['title'])
        article_text_formatted = article_convert(article_original.content)

        template = loader.get_template('wikipedia_converter/article.html')

        # use the formatted text but for title, link, ... the standard WikipediaPage object
        context = {
            'article': article_original,
            'article_text_formatted': article_text_formatted,
        }

        return HttpResponse(template.render(context, request))

    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        original_search_request = request.POST['title']

        template = loader.get_template('wikipedia_converter/options.html')

        context = {
            'original_search_request': original_search_request,
            'options': options,
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


def save_article(request):
    title = request.POST['title']

    article_original = wikipedia.page(title)
    article_formatted = article_convert(article_original.content)

    article_original = Article(content=article_original.content,
                               link=article_original.url,
                               title=article_original.title)

    article_original.save()

    article_formatted = Article(content=article_formatted,
                                link=article_original.link,
                                title=article_original.title)

    article_formatted.save()

    date = timezone.now()

    full_article = FullArticle(formatted_page=article_formatted,
                               original_page=article_original,
                               date_pulled=date)

    full_article.save()

    return HttpResponseRedirect(reverse('wikipedia_converter:Index'))


def get_article_from_db(request, pk):
    article1 = FullArticle.objects.get(pk=pk)

    template = loader.get_template('wikipedia_converter/article.html')

    context = {
        'article': article1.original_page,
        'article_text_formatted': article1.formatted_page.content
    }

    return HttpResponse(template.render(context, request))

def delete_article_from_db(request, pk):
    article = request.POST['article']
