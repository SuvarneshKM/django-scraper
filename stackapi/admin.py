from django.contrib import admin

# Register your models here.

from .models import Price, Pricesilver

admin.site.register(Price)
admin.site.register(Pricesilver)