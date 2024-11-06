from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from friendship.models import Friend, FriendshipRequest

from feeds.views import own_feed, create_base_feed_response
from takes.models import Take
from .forms import UpdateUserprofileForm, UpdateUserForm


def public_profile(request: HttpRequest, profile_id: str) -> HttpResponse:
    user: User = User.objects.get(pk=profile_id)

    are_friends = Friend.objects.are_friends(user, request.user)
    if are_friends:
        takes = Take.objects.filter(author=user, reply_to__isnull=True).order_by('-date')
    else:
        takes = Take.objects.filter(author=user, reply_to__isnull=True, is_public=True).order_by('-date')

    takes_list = create_base_feed_response(request, takes, 'Takes', 'take-page', None)
    takes_list.render()

    return render(request, 'userprofile-public.html',
                  {
                      'takes_list': takes_list.rendered_content,
                      'user': user,
                  })


@login_required
def add_friend(request: HttpRequest, user_id: str) -> HttpResponse:
    other_user: User = User.objects.get(pk=user_id)
    Friend.objects.add_friend(request.user, other_user)

    messages.success(request, 'Friend request send')

    return HttpResponseRedirect(reverse('userprofile:public_profile', kwargs={'profile_id': user_id}))


@login_required
def accept_friend(request: HttpRequest, user_id: str) -> HttpResponse:
    other_user: User = User.objects.get(pk=user_id)
    friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user)
    friend_request.accept()

    messages.success(request, 'Friend request accepted')

    return HttpResponseRedirect(reverse('userprofile:friends'))


@login_required
def reject_friend(request: HttpRequest, user_id: str) -> HttpResponse:
    other_user: User = User.objects.get(pk=user_id)
    friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user)
    friend_request.reject()

    messages.success(request, 'Friend request rejected')

    return HttpResponseRedirect(reverse('userprofile:friends'))


@login_required
def remove_friend(request: HttpRequest, user_id: str) -> HttpResponse:
    other_user: User = User.objects.get(pk=user_id)
    Friend.objects.remove_friend(request.user, other_user)

    messages.success(request, 'Friend removed')

    return HttpResponseRedirect(reverse('userprofile:friends'))


@login_required
def profile_edit(request: HttpRequest) -> HttpResponse:
    user = request.user

    own_feed_view = own_feed(request)
    own_feed_view.render()

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateUserprofileForm(request.POST, request.FILES, instance=user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated.')
    else:
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateUserprofileForm(instance=user.userprofile)

    return render(request, 'userprofile-edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'own_feed': own_feed_view.rendered_content,
    })


@login_required
def friends(request: HttpRequest) -> HttpResponse:
    friend_requests = FriendshipRequest.objects.filter(to_user=request.user)
    friends = Friend.objects.friends(request.user)

    return render(request, 'userprofile-friends.html',
                  {
                      'friends': friends,
                      'friend_requests': friend_requests,
                  })
