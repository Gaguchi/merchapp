from django.db import models

# Create your models here.

class shops_SPB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='shop_images')
    url = models.URLField()
    
class supermarkets_SPB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='shop_images')
    url = models.URLField()

class brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='brand_images')

class product(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=False)
    image = models.ImageField(upload_to='product_images')
    box = models.IntegerField()
    barcode = models.ImageField(upload_to='product_barcodes')

class perek_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class pyaterechka_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class briz_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class vkuster_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class plovdiv_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class rosneft_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class dixy_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class prisma_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class vernyi_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class magnit_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class lenta_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class auchan_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)
    
class ok_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    priority = models.IntegerField(unique=True)