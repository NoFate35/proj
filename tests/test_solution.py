import pytest

from catalog import Catalog


def test_catalog(db_transaction):
    catalog = Catalog(db_transaction)
    actual = catalog.get_product('banana')
    assert actual['name'] == 'banana'
    assert actual['description'] == 'yellow fruit'
    assert actual['price'] == 50

    actual2 = catalog.get_product('strawberry')
    assert actual2['name'] == 'strawberry'
    assert actual2['description'] == 'small red fruit'
    assert actual2['price'] == 70


def test_not_found_product(db_transaction):
    catalog = Catalog(db_transaction)
    with pytest.raises(KeyError):
        catalog.get_product('not existed product')
