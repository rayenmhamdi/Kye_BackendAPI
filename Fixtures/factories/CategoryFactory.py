import random
import string

import factory
from faker import Faker

from article.models import Category


#http://zetcode.com/python/faker/
def get_random_string(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))

def create_category():
    fake = Faker()
    c = Category(code=get_random_string(3), name = fake.company())
    c.save()