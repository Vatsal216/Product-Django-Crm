from django.db import models
from tangled_up_in_unicode import name

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=10)
    description=models.TextField()
    type=models.CharField(max_length=10)


class ProductDetails(models.Model):
    product=models.ForeignKey(Product)
    processor=models.CharField(max_length=10)
    ram = models.CharField(max_length=10)
    screen_size=models.CharField(max_length=10)
    color=models.CharField(max_length=10)
    Hd_capacity=models.CharField(max_length=10)
    

