import pytest

import app


# A Fixture is utility provided by pytest to set up our test environment for different scope
# E.g. session, module or function - depending on when the environment need to be created and teared down
@pytest.fixture(scope="function")
def calculator():
    return app.Calculator()


def test_append(calculator):
    with pytest.raises(ValueError):
        calculator.sum()