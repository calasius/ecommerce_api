import pytest

from ecommerce.user.models import User


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """Fixture to execute asserts before and after each test"""

    from conf_test_db import override_get_db

    database = next(override_get_db())
    new_user = User(name="John Doe", email="john@gmail.com", password="123456")
    database.add(new_user)
    database.commit()

    yield  # This is where the testing happens

    # This is where the cleanup happens
    database.query(User).filter(User.email == "john@gmail.com").delete()
    database.commit()
