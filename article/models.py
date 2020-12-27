from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)


class Product(models.Model):
    bar_code = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=20, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    min_quantity_alert = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('unavailable', 'Unavailable'),
        ('available', 'Available'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, null=False, blank=False)
    details = models.TextField(max_length=1000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


class ProductHistory(models.Model):
    pass



