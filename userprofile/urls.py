from django.urls import path

from . import views

app_name = 'userprofile'

urlpatterns = [
    path('edit', views.profile_edit, name='edit'),
    path('friends/invite/<str:user_id>', views.add_friend, name='friend_add'),
    path('friends/reject/<str:user_id>', views.reject_friend, name='friend_reject'),
    path('friends/accept/<str:user_id>', views.accept_friend, name='friend_accept'),
    path('friends/remove/<str:user_id>', views.remove_friend, name='friend_remove'),
    path('friends', views.friends, name='friends'),
    path('public/<str:profile_id>', views.public_profile, name='public_profile'),
]
