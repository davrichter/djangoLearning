from django.template import loader
from django.views import generic
from django.http import HttpResponse

import wikipedia

from .models import Article


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'wikipedia_converter/index.html'
    context_object_name = 'old_articles'

    def get_queryset(self):
        return Article.objects.all()


def get_articles(request):
    search = request.POST['search']

    # if searching for empty string dont search for it on wikipedia
    # that will return an error just assign it to an empty array
    if search != "":
        search_results = wikipedia.search(request.POST['search'])
    else:
        search_results = []

    template = loader.get_template('wikipedia_converter/search_results.html')
    context = {
        'search': search,
        'search_results': search_results,
    }

    return HttpResponse(template.render(context, request))
