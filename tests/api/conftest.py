import pytest

from api.user_api import GorestUser


@pytest.fixture
def gorest_user():
    return GorestUser()