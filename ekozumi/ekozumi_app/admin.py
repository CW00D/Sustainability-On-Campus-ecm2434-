"""
This file is mainly used to display our models on the admin page
allowing for easy modification
"""

from django.contrib import admin
from .models import Profile, Pet, Monster

# Models which are displayed in the admin panel
# Register your models here.
admin.site.register(Profile)
admin.site.register(Pet)
admin.site.register(Monster)