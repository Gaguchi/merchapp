from django.db import models

# Create your models here.
class cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)

class shops(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    city = models.ForeignKey(cities, on_delete=models.CASCADE)

class brands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='brand_images')

class product(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=False)
    image = models.ImageField(upload_to='product_images')
    box = models.IntegerField()
    barcode = models.ImageField(upload_to='product_barcodes')
