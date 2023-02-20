import pytest

# from django.contrib.auth.models import User

# # access to DB with pytest
# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test', 'test@test.com', 'test')
#     count = User.objects.all().count()
#     print(count)
#     assert User.objects.count() == 1

# # in this way the user we made befor doesn't exist so count must be 0
# @pytest.mark.django_db
# def test_user_create1():
#     count = User.objects.all().count()
#     print(count)
#     assert count == 0

# access to the database with fixture
# here we cann't use scope="session"
# @pytest.fixture
# def userr(db):
#     user = User.objects.create_user('new-user')
#     return user

# these are tests for the application
# when connect to db with fixture we can access previous data easily
def test_set_new_password(user):
    user.set_password("pass")
    print("ok")
    assert user.check_password("pass") is True

def test_set_check_username(user):
    print('Oh nanana...')
    assert user.username == 'new-user'

def test_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name == "fname"