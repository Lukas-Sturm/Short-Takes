from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('simple', views.simple, name='simple'),
]
