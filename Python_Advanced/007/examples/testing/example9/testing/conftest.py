import pytest
from models import User


# фікстура різних рівнів
# session – завжди буде однакова в рамках сесії
# module - буде однаковою лише в рамках модуля
# class - буде однакова у межах клас
# function - буде однаковою в рамках функції/методу
@pytest.fixture(scope='session')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='function')
# @pytest.fixture
def user():
    return User(
        email='test@example.com',
        first_name='test1',
        last_name='test2',
        fixture=True
    )
