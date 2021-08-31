from django.db import models

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
    user = models.ForeignKey('accounts.User', on_delete=models.RESTRICT)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    order_number = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=3, decimal_places=0)
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
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
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


class ShippingCompany(models.Model):
    company_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    postal_code = models.CharField(max_length=50)
    county = models.ForeignKey(County, on_delete=models.RESTRICT)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class ShippingInformation(models.Model):
    delivery = models.ForeignKey(DeliveryInformation, on_delete=models.RESTRICT)
    shipping_company = models.ForeignKey(ShippingCompany, on_delete=models.RESTRICT)
    delivery_date = models.DateTimeField()
    courier_phone_number = models.CharField(max_length=11)
    client_phone_number = models.CharField(max_length=11)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    postal_code = models.CharField(max_length=50)
    county = models.ForeignKey(County, on_delete=models.RESTRICT)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.delivery_date
