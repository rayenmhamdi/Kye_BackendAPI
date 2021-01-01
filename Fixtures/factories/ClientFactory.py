import factory

from crm.models import Client

#http://zetcode.com/python/faker/
class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client
    name = factory.Faker('name')
    phone_1 = factory.Faker('phone_number')
    phone_2 = factory.Faker('phone_number')
    address = factory.Faker('address')
    email = factory.Faker('company_email')
