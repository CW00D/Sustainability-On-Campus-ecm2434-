"""
This file is mainly used to display our models on the admin page
allowing for easy modification
"""

from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.register(Profile)