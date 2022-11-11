from django.contrib import admin
from .models import *


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'publish_date']
