from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()


