from django.contrib import admin

# Register your models here.
from crm.models import Client, Supplier

admin.site.register(Client)
admin.site.register(Supplier)
