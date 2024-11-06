import os
import random

from PIL import Image, ImageDraw, ImageOps
from django.core.files.images import ImageFile
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from short_takes import settings
from .models import Userprofile
from .voronoi import generate, ColorAlgorithm, DistanceAlgorithm

colors = [
    ["#78c9b1", "#3eab71", "#27904d", "#006127"],
    ["#1d63db", "#155ad0", "#0c4dbd", "#10459f"],
    ["#ff7b00", "#ff9500", "#ffb700", "#ffea00"],
    ["#91db57", "#57d3db", "#5770db", "#a157db"]
]

@receiver(post_save, sender=User)
def create_userprofile(sender, instance: User, created, **kwargs):
    if created:
        userprofile = Userprofile.objects.create(user=instance)

        profile_image = generate(
            regions=8,
            colors=random.choice(colors),
            color_algorithm=ColorAlgorithm.no_adjacent_same,
            distance_algorithm=random.choice([DistanceAlgorithm.manhattan, DistanceAlgorithm.euclidean]),
            width=100,
            height=100,
            border_size=random.randint(0, 3),
        )

        # https://stackoverflow.com/questions/890051/how-do-i-generate-circular-thumbnails-with-pil
        size = (100, 100)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)

        profile_image_cut = ImageOps.fit(profile_image, mask.size, centering=(0.5, 0.5))
        profile_image_cut.putalpha(mask)
        profile_image_cut.resize((150, 150))

        profile_image_path = os.path.join(settings.PROFILE_IMAGES_PATH, f'temp_profile_image_generated.png')
        profile_image_cut.save(profile_image_path)

        with open(profile_image_path, 'rb') as f:
            userprofile.avatar = ImageFile(f)
            userprofile.save()
