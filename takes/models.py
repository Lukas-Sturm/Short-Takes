import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class Take(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_public = models.BooleanField(default=True)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    date = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    liked_by = models.ManyToManyField(User, blank=True, related_name='liked_by')
    disliked_by = models.ManyToManyField(User, blank=True, related_name='disliked_by')

    def replies(self, requesting_user: User, root_author: User):
        """Loads replies for this Take, this respects visibility
        If someone replies to a Take with a private take but is not friends with the Author
        of the original Take, the Author will still be able to see the Take and all its replies
        """
        if requesting_user == root_author:
            return Take.objects.filter(reply_to__id=self.id)

        if not requesting_user.is_authenticated:
            # anonymous user can't have friends
            return Take.objects.filter(Q(reply_to__id=self.id) & Q(is_public=True))

        return Take.objects.filter(
            # is_public=False this removes duplicates, if they are friends, but it is public both would return this.
            # PEP format is crazy on this one
            (Q(reply_to__id=self.id) & (
                        Q(author__friends__from_user=requesting_user) | Q(author_id=requesting_user.id)) & Q(
                is_public=False))
            |
            (Q(reply_to__id=self.id) & Q(is_public=True))
        ).distinct()

    def reply_count(self):
        return Take.objects.filter(reply_to_id=self.id).count()

    def __str__(self):
        return f'Take={self.id}'
