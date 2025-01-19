from music_service import MusicService

import pytest
import psycopg2
import psycopg2.extras


@pytest.fixture(scope="session")
def db_connection():
    """conn = psycopg2.connect(dbname='hexlet', user='ivan',  host='/var/run/postgresql')"""
    conn = psycopg2.connect(dbname='hexlet', user='u0_a440',  host='/data/data/com.termux/files/usr/tmp')
    #print('yeeeeessssss')
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




def test_music_service_1(db_transaction):
    service = MusicService(db_transaction)
    actual = service.get_song_by_title('are')

    assert len(actual) == 2

    song1 = actual[0]
    assert song1.title == 'They Are With Me'

    song2 = actual[1]
    assert song2.title == 'You are Not Like That'


def test_music_service_2(db_transaction):
    service = MusicService(db_transaction)
    actual = service.get_song_by_title('st')

    assert len(actual) == 2

    song1 = actual[0]
    assert song1.title == 'Starry Rain'

    song2 = actual[1]
    assert song2.title == 'The Best Day'


def test_song_not_found(db_transaction):
    service = MusicService(db_transaction)
    actual = service.get_song_by_title('NotExists')

    assert actual == []
