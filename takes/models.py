import uuid

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Tag={self.id}-{self.name}'


# Create your models here.
class Take(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_public = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    content = models.TextField(max_length=2000)
    tags = models.ManyToManyField('Tag', blank=True)
    # images = models.ManyToManyField(Image, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Take={self.id}'
