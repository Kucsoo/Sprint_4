import pytest
import helpers



@pytest.fixture
def name():
    name = helpers.random_name()
    return name
@pytest.fixture
def surname():
    surname = helpers.random_surname()
    return surname

@pytest.fixture
def address():
    address = helpers.random_address()
    return address

@pytest.fixture
def telephone():
    telephone = helpers.random_telephone()
    return telephone

@pytest.fixture
def comment():
    comment = helpers.random_comment()
    return comment