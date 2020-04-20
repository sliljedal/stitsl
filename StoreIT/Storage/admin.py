from django.contrib import admin
from .models import Item, Storage, Box

admin.site.register(Item)
admin.site.register(Box)
admin.site.register(Storage)
