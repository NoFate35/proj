import pytest

from car_base import CarBase


def test_car_base(db_transaction):
    car_base = CarBase(db_transaction)
    actual = car_base.get_info('123ab')

    assert actual["manufacturer"] == "Ford"
    assert actual["model"] == "E350"
    assert actual["owner"] == "Raine Wrennall"
    assert actual["owner_address"] == "08 Arkansas Plaza"

    actual2 = car_base.get_info('nm759')

    assert actual2["manufacturer"] == "Ford"
    assert actual2["model"] == "Taurus"
    assert actual2["owner"] == "Sunshine Fairbourn"
    assert actual2["owner_address"] == "48395 Graedel Parkway"


def test_non_exists_car(db_transaction):
    car_base = CarBase(db_transaction)

    with pytest.raises(KeyError):
        car_base.get_info("non_exist")
