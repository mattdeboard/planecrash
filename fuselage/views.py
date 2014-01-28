from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

from .models import Article, Category


@require_http_methods(["GET"])
def index(request):
    # Keeping this dead simple for now: one query per category.
    articles = {}

    for cat in Category.objects.values_list('short_name', flat=True):
        _articles = Article.objects.by_category(cat)

        if _articles.count():
            articles[cat] = _articles

    return render_to_response('index.html', {'articles': articles},
                              context_instance=RequestContext(request))
