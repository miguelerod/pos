from django.contrib import admin
from .models.models import Item, Invoice, Order

# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Invoice)
