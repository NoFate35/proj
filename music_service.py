from songDAO import SongDAO


# BEGIN (write your solution here)
class MusicService:
    def __init__(self, conn):
        self.conn = conn
    def get_song_by_title(self, letters):
        dao = SongDAO(self.conn)
        result = dao.find_song(letters)
        return result
        print('result', result)
# END