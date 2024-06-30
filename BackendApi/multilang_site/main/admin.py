from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin

# Register your models here.

admin.site.register(Post, TranslatableAdmin)