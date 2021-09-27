from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Hero)
admin.site.register(User)
