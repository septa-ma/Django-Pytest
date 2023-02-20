# all fixtures write here
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user(db):
    user = User.objects.create_user('new-user')
    print("new-user")
    return user

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = 'FName',
        last_name: str = 'LName',
        email: str = 'email@n.com',
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user

@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory("test","pass","fname","lname")