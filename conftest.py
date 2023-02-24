# all fixtures write here
import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, ProductFactory, CategoryFactory
from django.contrib.auth.models import User

register(UserFactory) # the fixture is user_factory
register(CategoryFactory)
register(ProductFactory)

@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.build() # produce an  object, count is 0
    # user = user_factory.create() # save data to our test db, count is 1
    count = User.objects.all().count()
    return user, count

@pytest.fixture
def new_product(db, product_factory):
    # product = product_factory.build()
    product = product_factory.create()
    return product