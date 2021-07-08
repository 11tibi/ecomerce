from django.db import models
from accounts.models import User

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    active = models.BooleanField()
    discount_percent = models.DecimalField(max_digits=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.active


class Inventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quantity


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.RESTRICT)
    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT)
    inventory = models.ForeignKey(Inventory, on_delete=models.RESTRICT)
    link = models.CharField(max_length=100)
    price = models.FloatField()
    SKU = models.CharField(max_length=50, unique=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=100)
    prod = models.ForeignKey(Product, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image


class Specs(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} : {self.description}"


class Reviews(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    description = models.TextField()
    rating = models.DecimalField(max_digits=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
