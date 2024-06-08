from django.urls import path

from . import views

app_name = 'feeds'

urlpatterns = [
    path("public", views.public, name="public"),
    path("private", views.private, name="private"),
]