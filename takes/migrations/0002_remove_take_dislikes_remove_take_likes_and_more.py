# Generated by Django 5.0.6 on 2024-07-09 04:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='take',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='take',
            name='likes',
        ),
        migrations.AddField(
            model_name='take',
            name='disliked_by',
            field=models.ManyToManyField(blank=True, related_name='disliked_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='take',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='take',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
