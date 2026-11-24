import os

import pytest

@pytest.fixture
def username():
    user_login = os.getenv("LOGIN")
    assert user_login is not None, "Please set LOGIN environment variable"
    return user_login

@pytest.fixture
def password():
    password = os.getenv("PASSWORD")
    assert password is not None, "Please set PASSWORD environment variable"
    return password
