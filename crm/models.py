from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_1 = models.PositiveIntegerField(blank=True, null=True)
    phone_2 = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}: {}".format(self.id, self.name)


class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_1 = models.PositiveIntegerField(blank=True, null=True)
    phone_2 = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}: {}".format(self.id, self.name)