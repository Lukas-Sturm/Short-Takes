from django import template
from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest

from takes.models import Take

register = template.Library()


@register.filter
def dict_key(d, k):
    """Returns the given key from a dictionary."""
    # this is only needed because form errors uses __all__ but . notation can't access _ property
    return d[k]


@register.filter
def extract_error_from_dict(errors, key):
    if not errors:
        return []
    if key in errors:
        return errors[key]
    return []


@register.simple_tag
def user_liked(user: User, take: Take):
    return take.liked_by.contains(user)


@register.simple_tag
def user_disliked(user: User, take: Take):
    return take.disliked_by.contains(user)


@register.simple_tag
def users_are_friends(from_user: User, to_user: User):
    if FriendshipRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
        return True

    return Friend.objects.are_friends(from_user, to_user)


@register.simple_tag
def load_allowed_replies(take: Take, user: User, root_author: User):
    return take.replies(user, root_author)
