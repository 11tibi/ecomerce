from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class County(models.Model):
    county = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.county


class City(models.Model):
    county = models.ForeignKey(County, on_delete=models.RESTRICT, null=False)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Order(models.Model):

    class CustomerType(models.TextChoices):
        PERSON = 'F', _('Person')
        COMPANY = 'C', _('Company')

    user = models.ForeignKey('accounts.User', on_delete=models.RESTRICT)
    AWB = models.CharField(max_length=11)
    customer_type = models.CharField(max_length=1, choices=CustomerType.choices, default=CustomerType.PERSON)
    phone_number = models.CharField(max_length=11)
    order_number = models.CharField(max_length=100)
    shipping_cost = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.total


class OrderItems(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quantity


class Deposit(models.Model):
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    county = models.ForeignKey(County, on_delete=models.RESTRICT)
    postal_code = models.CharField(max_length=6)
    street = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city


class DeliveryInformation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    deposit = models.ForeignKey(Deposit, on_delete=models.RESTRICT)
    require_shipping = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.require_shipping


class ShippingInformation(models.Model):
    delivery = models.ForeignKey(DeliveryInformation, on_delete=models.RESTRICT)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    county = models.ForeignKey(County, on_delete=models.RESTRICT)
    street = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=6)
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.delivery_date


class CompanyInformation(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.RESTRICT)
    company_name = models.CharField(max_length=100)
    company_reg_no = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    IBAN = models.CharField(max_length=15)
    fiscal_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
