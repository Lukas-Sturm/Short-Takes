from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def public(request: HttpRequest) -> HttpResponse:
    return render(request, 'feeds-public.html')


def private(request: HttpRequest) -> HttpResponse:
    return render(request, 'feeds-private.html')
