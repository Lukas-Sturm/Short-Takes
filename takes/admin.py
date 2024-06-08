from django.contrib import admin

# Register your models here.

from .models import Tag, Take

admin.site.register(Tag)
admin.site.register(Take)
