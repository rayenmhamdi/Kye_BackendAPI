from django.utils.datetime_safe import datetime

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Marque(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    @property
    def product_number(self):
        return self.products.count()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    bar_code = models.CharField(max_length=50, null=True, blank=True, unique=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    marque = models.CharField(max_length=50, null=True, blank=True)

    vat = models.DecimalField(max_digits=30, decimal_places=5, default=0.0, validators=[MinValueValidator(0)], null=False, blank=False)
    purchase_price_without_tax = models.DecimalField(max_digits=30, decimal_places=5, default=0.0, validators=[MinValueValidator(0)], null=False, blank=False)
    purchase_price = models.DecimalField(max_digits=30, decimal_places=5, default=0.0, validators=[MinValueValidator(0)], null=False, blank=False)
    sale_price_without_tax = models.DecimalField(max_digits=30, decimal_places=5, default=0.0, validators=[MinValueValidator(0)], null=False, blank=False)
    sale_price = models.DecimalField(max_digits=30, decimal_places=5, default=0.0, validators=[MinValueValidator(0)], null=False, blank=False)
    marge = models.DecimalField(max_digits=30, decimal_places=5, default=0.0, validators=[MinValueValidator(0)], null=False, blank=False)

    quantity = models.PositiveIntegerField(default=0, null=False, blank=False)
    min_quantity_alert = models.PositiveIntegerField(default=0, null=False, blank=False)
    STATUS_CHOICES = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, null=False, blank=False)
    details = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)



class ProductHistory(models.Model):
    pass



