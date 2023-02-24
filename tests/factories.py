import factory
from faker import Faker
from django.contrib.auth.models import User
from core.app import models

fake = Faker()
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'

# make factory for models with Foreign Key
# if a model has FK:
# 1- first initial refrence model then.
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = 'my_category'

# 2- second use factory.SubFactory(CategoryFactory) for the FK field.
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    category = factory.SubFactory(CategoryFactory) 
    description = fake.text()
    price = '9.99'
    title = 'my_title'