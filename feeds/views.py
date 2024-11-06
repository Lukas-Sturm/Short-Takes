from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _

from takes.models import Take


def public_feed(request: HttpRequest, retain_pagination=None) -> TemplateResponse:
    """Generates a Template Response for the public feed of the current User.
    Currently very basic, only shows Takes ordered by date."""
    takes = Take.objects.filter(is_public=True, reply_to__isnull=True).order_by('-date')
    return create_base_feed_response(request, takes, _('Public Takes'), 'public-feed', retain_pagination)


def private_feed(request: HttpRequest, retain_pagination=None) -> TemplateResponse:
    """Generates a Template Response for the private feed of the current User.
    Currently very basic, only shows Takes ordered by date created by friends of the current User."""
    takes = Take.objects.filter(author__friends__from_user=request.user, is_public=False, reply_to__isnull=True).order_by('-date')
    return create_base_feed_response(request, takes, _('Your Feed'), 'private-feed', retain_pagination)


def own_feed(request: HttpRequest, retain_pagination=None) -> TemplateResponse:
    """Generates a Template Response for the all Takes of the current User ordered by date."""
    takes = Take.objects.filter(author=request.user).order_by('-date')
    return create_base_feed_response(request, takes, _('Your Takes'), 'own-feed', retain_pagination)


def create_base_feed_response(request: HttpRequest,
                              query_set: QuerySet,
                              feed_title: str,
                              pagination_parameter,
                              persistent_url_parameter: dict | None,
                              template_name='feeds-base.html',
                              ) -> TemplateResponse:
    """Creates a Template Response for a set of Takes. Handles Pagination."""
    paginator = Paginator(query_set, 5)
    page_number = request.GET.get(pagination_parameter)
    page = paginator.get_page(page_number)

    # filter and build pagination parameter
    url_parameter = ''
    if persistent_url_parameter:
        url_parameter = [
            '{}={}'.format(key, value) for (key, value) in persistent_url_parameter.items() if not key == pagination_parameter
        ]
        url_parameter = "&".join(url_parameter)

    return TemplateResponse(request, template_name, {
        'feed_name': feed_title,
        'takes_page': page,
        'pagination_parameter': pagination_parameter,
        'url_parameter': url_parameter,
        'pagination_num_pages': paginator.num_pages
    })
