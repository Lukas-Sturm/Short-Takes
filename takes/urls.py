from django.urls import path

from . import views

app_name = 'takes'

urlpatterns = [
    path("<str:take_id>/", views.take, name="take"),
]