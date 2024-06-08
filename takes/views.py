from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def take(request: HttpRequest, take_id: str) -> HttpResponse:
    return HttpResponse(f"This is a Take {take_id}")
