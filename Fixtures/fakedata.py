import os

import factory
from autofixture import AutoFixture

from Fixtures.factories.CategoryFactory import create_category
from Fixtures.factories.ProductFactory import create_products
from Fixtures.factories.SupplierFactory import SupplierFactory
from Fixtures.factories.ClientFactory import ClientFactory
from Fixtures.factories.MarqueFactory import MarqueFactory
from article.models import Marque, Category, Product
from crm.models import Client, Supplier

"""
Models:
    Access (load directly from fixture json file):
        KyeUser
        Profile
        Store
        Licence
    Crm:
        Client
        Supplier
    Article:
        Marque
        Category
        Product
"""
def generate_data():
    # reset ids

    #generate 100 Clients
    Client.objects.all().delete()
    for _ in range(100):
        ClientFactory.create()
    print('100 Client generated')

    # generate 30 Supplier
    Supplier.objects.all().delete()
    for _ in range(30):
        SupplierFactory.create()
    print('30 Supplier generated')

    # Delete Products
    Product.objects.all().delete()

    # Generate 10 Marques
    Marque.objects.all().delete()
    for _ in range(10):
        MarqueFactory.create()
    print('10 Marque generated')


    #Delete Categories
    # Generate 20 Category
    Category.objects.all().delete()
    category_generated_number = 0
    while category_generated_number < 20:
        try:
            create_category()
            category_generated_number += 1
        except Exception as e:
            print(e)
    print('20 Category generated')

    #Generate Products
    create_products(500)
    print('500 Product generated')

