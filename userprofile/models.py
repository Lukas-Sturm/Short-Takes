from PIL import Image
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from short_takes import settings

import os


def _safe_upload_filename(instance, filename):
    extension = ''
    split = filename.split('.')
    if len(split) > 1:
        extension = f'.{split[-1]}'
    return os.path.join(
        settings.PROFILE_IMAGES_PATH, f'{instance.user.id.__str__()}{extension}'
    )


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default-profile.png', upload_to=_safe_upload_filename)
    bio = models.TextField()

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)
        if img.height > 150 or img.width > 150:
            new_size = (150, 150)
            img.thumbnail(new_size)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username
