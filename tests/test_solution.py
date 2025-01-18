from music_service import MusicService


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
