from django.contrib import admin
from .models import Warehouse,Product,Stock

# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Product)
admin.site.register(Stock)
