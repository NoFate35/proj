import pytest

from car_base import CarBase
import pytest
import psycopg2
import psycopg2.extras


@pytest.fixture(scope="session")
def db_connection1():
    #conn = psycopg2.connect(dbname='hexlet', user='ivan',  host='/var/run/postgresql')
    conn = psycopg2.connect(dbname='hexlet', user='u0_a440',  host='/data/data/com.termux/files/usr/tmp')
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def db_transaction1(db_connection1):
    with db_connection1:
        with db_connection1.cursor() as cur:
            cur.execute("BEGIN")
            yield db_connection1
            cur.execute("ROLLBACK")

def test_car_base(db_transaction1):
    car_base = CarBase(db_transaction1)
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


def test_non_exists_car(db_transaction1):
    car_base = CarBase(db_transaction1)

    with pytest.raises(KeyError):
        car_base.get_info("non_exist")
