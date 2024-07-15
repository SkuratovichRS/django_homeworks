from django.db.models import Prefetch
from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    objects_list = Article.objects.order_by(ordering).prefetch_related(
        Prefetch(
            'scopes',
            queryset=Scope.objects.order_by('-is_main', 'tag__name').select_related('tag'))
    )
    context = {"object_list": objects_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
