import factory

from crm.models import Supplier

#http://zetcode.com/python/faker/
class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier
    name = factory.Faker('name')
    phone_1 = str(factory.Faker('phone_number'))
    phone_2 = str(factory.Faker('phone_number'))
    address = factory.Faker('address')
    email = factory.Faker('company_email')