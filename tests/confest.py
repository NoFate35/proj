import pytest
import psycopg2
import psycopg2.extras


@pytest.fixture(scope="session")
def db_connection():
    """conn = psycopg2.connect(dbname='hexlet', user='ivan',  host='/var/run/postgresql')"""
    conn = psycopg2.connect(dbname='hexlet', user='u0_a440',  host='/data/data/com.termux/files/usr/tmp')
    print('yeeeeessssss')
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def db_transaction(db_connection):
    with db_connection:
        with db_connection.cursor() as cur:
            cur.execute("BEGIN")
            yield db_connection
            cur.execute("ROLLBACK")

