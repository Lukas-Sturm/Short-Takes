from django.urls import path

from . import views

app_name = 'takes'

urlpatterns = [
    path('view/<str:take_id>', views.view, name='take'),
    path('create', views.create, name='create'),
    path('reply/<str:reply_to_id>', views.reply, name='reply'),
    path('delete/<str:take_id>', views.delete, name='delete'),

    path('like/<str:take_id>', views.like, name='up_vote'),
    path('dislike/<str:take_id>', views.dislike, name='down_vote'),
]
