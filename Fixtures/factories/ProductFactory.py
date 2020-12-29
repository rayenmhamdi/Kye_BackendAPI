import random
import string

import factory
from faker import Faker

from article.models import Category, Marque, Product


#http://zetcode.com/python/faker/

def create_products(number):
    fake = Faker()
    generated_number = 0
    for _ in range(number):
        while generated_number < number:
            try:
                categories = Category.objects.all()
                marques = Marque.objects.all()

                category = random.choice(categories)
                code = category.code + str(category.product_number).zfill(5)
                bar_code = fake.ean(length=13)
                name = fake.name()
                marque = random.choice([None, (random.choice(marques)).name])
                vat = random.choice([19, 7])
                purchase_without_tax = random.randrange(1000, 500000) / 100
                purchase_price = purchase_without_tax + (purchase_without_tax * vat) / 100

                sale_price_without_tax = purchase_without_tax + random.randrange(100, 50000) / 100
                sale_price = sale_price_without_tax + (sale_price_without_tax * vat) / 100
                marge = ((sale_price - purchase_price) / purchase_price) * 100

                quantity = 0
                min_quantity_alert = random.choice([0, random.randint(1, 20)])
                status = 'active'
                details = random.choice([None, fake.sentence(nb_words=10)])

                p = Product(
                    category=category,
                    code=code,
                    bar_code=bar_code,
                    name=name,
                    marque=marque,
                    vat=vat,
                    purchase_price_without_tax=purchase_without_tax,
                    purchase_price=purchase_price,
                    sale_price_without_tax=sale_price_without_tax,
                    sale_price=sale_price,
                    marge=marge,
                    quantity=quantity,
                    min_quantity_alert=min_quantity_alert,
                    status=status,
                    details=details
                )

                p.save()
                generated_number += 1
            except Exception as e:
                print(e)