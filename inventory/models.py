from django.db import models

# Create your models here.

class Warehouse(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    sku=models.CharField(unique=True,max_length=50)
    
    def __str__(self):
        return self.name
