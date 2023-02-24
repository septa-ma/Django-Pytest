import pytest
# from django.contrib.auth.models import User

# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.build() # produce an  object, count is 0
#     # user = user_factory.create() # save data to our test db, count is 1
#     count = User.objects.all().count()
#     print(count)
#     print(user_factory.username)
#     assert True

# def test_new_user(new_user):
#     print(new_user)
#     assert True

# def test_product(new_product):
#     print(new_product.title)
#     print(new_product.category)
#     print(new_product.description)
#     print(new_product.price)
#     assert True