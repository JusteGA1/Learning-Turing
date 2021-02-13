import pytest
from tesla.factory import Tesla


@pytest.fixture
def tesla():
    return Tesla('S', 'red')


def test_seats_count(tesla):
    assert tesla.seats_count == 5


def test_charge_battery(tesla):
    tesla.charge_battery()
    assert tesla.check_battery_level() == "Battery charge level is 100%"


def test_welcome(tesla):
    with pytest.raises(NotImplementedError):
        tesla.welcome()
