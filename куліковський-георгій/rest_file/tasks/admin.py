from django.contrib import admin

from .models import Task

admin.site.register(Task)

admin.site.site_header = "To do list admin page"
