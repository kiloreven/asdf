from django.contrib import admin
from django.db import models

from .models import Component, Position

admin.site.register(Component, admin.ModelAdmin)
admin.site.register(Position, admin.ModelAdmin)
