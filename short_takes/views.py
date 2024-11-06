from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from short_takes.forms import EmailEnabledUserCreationForm
from feeds.views import private_feed as priv_feed, public_feed as pub_feed


def index(request: HttpRequest) -> HttpResponse:
    current_url_parameter = request.GET.dict()
    public_feed = pub_feed(request, current_url_parameter)

    if request.user.is_authenticated:
        private_feed = priv_feed(request, current_url_parameter)  # retain all active url parameters. i.e public feed
        return render(request, 'short-takes-home.html',
                      {
                          'public_feed': public_feed.rendered_content,
                          'private_feed': None if private_feed is None else private_feed.rendered_content,
                      })

    return render(request, 'short-takes-landing.html',
                  {
                      'public_feed': public_feed.rendered_content,
                  })


def register(request: HttpRequest) -> HttpResponse:
    form = EmailEnabledUserCreationForm()

    if request.method == 'POST':
        form = EmailEnabledUserCreationForm(request.POST)
        if form.is_valid():
            user: User = form.save()
            login(request, user)

            return HttpResponseRedirect(reverse('index'))

    return render(request, 'auth/short-takes-register.html', {
        'register_form': form
    })
