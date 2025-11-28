from django.db import models
from django.contrib import admin
# Create your models here.
class Product(models.Model):
    id1= models.IntegerField(help_text="enter product id1:")
    id2= models.IntegerField(help_text="enter product id2:")
    name1= models.CharField(max_length=10, help_text="enter product name1:")
    name2= models.CharField(max_length=15, help_text="enter product name2:")

class ProductAdmin(admin.ModelAdmin):
    list_display=['id1','id2','name1','name2']
