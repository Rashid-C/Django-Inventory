from django.shortcuts import render
from .models import Warehouse

def warehouse_list(request):
    warehouse=Warehouse.objects.all()
    
    return render(request, 'inventory/warehouse_list.html', {'warehouses': warehouses})
