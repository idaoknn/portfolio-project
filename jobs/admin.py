from django.contrib import admin

# jobs/admin.py

from .models import Job

admin.site.register(Job)
