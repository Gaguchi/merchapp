from django.db import models
from datetime import date
from django.utils.html import mark_safe

# Create your models here.

class shops_SPB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='shop_images')
    url = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
    
class supermarkets_SPB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='shop_images')
    url = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class company(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='brand_images')

    def __str__(self):
        return f"{self.name}"

class brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    company = models.ForeignKey(company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class product(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=False, unique=True)
    image = models.ImageField(upload_to='product_images')
    def img_preview(self): #new
        return mark_safe(f'<img scr = "{self.image.url}" witdh = "300"/>')

    box = models.IntegerField()
    barcode = models.ImageField(upload_to='product_barcodes')

    def __str__(self):
        return f"{self.brand}: {self.name}"

class perek_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class peterechka_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class briz_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class vkuster_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class plovdiv_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class rosneft_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class dixy_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class prisma_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class vernyi_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class magnit_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class lenta_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class auchan_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"
    
class ok_spb(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    plu = models.IntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.product.brand.company.name}: {self.product.name}"