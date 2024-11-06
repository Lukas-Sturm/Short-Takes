from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q, QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _
from django_htmx.middleware import HtmxDetails

from feeds.views import create_base_feed_response
from takes.models import Take


@login_required
def simple(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        # post search term wins over get
        # just redirect to new page
        search_term = request.POST[('search_term')]
        return HttpResponseRedirect(reverse('search:simple') + '?q=' + search_term)

    search_term = request.GET.get('q', '')

    takes_pages = create_base_feed_response(
        request,
        _search_takes(search_term, request.user),
        _('Takes search results'),
        'search-feed',
        {'q': search_term}
    )
    takes_pages.render()

    users = _search_users(search_term)

    if hasattr(request, 'htmx'):
        htmx: HtmxDetails = request.htmx
        if htmx.trigger == 'search_term':
            return render(request, 'search-simple-results.html', {
                'search_feed': takes_pages.rendered_content,
                'users': users,
            })

    return render(request, 'search-simple.html', {
        'search_term': search_term,
        'search_feed': takes_pages.rendered_content,
        'users': users,
    })


def _search_users(search_term: str) -> QuerySet:
    # Perform simple "like" query. This is fine for usernames. Trigrams would be better.
    if not search_term:
        return User.objects.none()
    return User.objects.filter(username__icontains=search_term)


def _search_takes(search_term: str, as_user: User) -> QuerySet:
    return Take.objects.filter(
        # any public takes
        (Q(content__search=search_term) & Q(is_public=True))
        |
        # takes of users friends is_public=False to avoid duplicates
        (Q(content__search=search_term) & Q(author__friends__from_user=as_user) & Q(is_public=False))
        |
        # own takes is_public=False to avoid duplicates
        (Q(content__search=search_term) & Q(author=as_user) & Q(is_public=False))
    ).order_by(
        'id'
    )
