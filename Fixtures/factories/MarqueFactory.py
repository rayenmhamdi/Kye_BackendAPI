import factory

from article.models import Marque

#http://zetcode.com/python/faker/
class MarqueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Marque
    name = factory.Faker('company')