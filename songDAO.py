from song import Song
from psycopg2.extras import NamedTupleCursor


# BEGIN (write your solution here)
class SongDAO:
    def __init__(self, conn):
        self.conn = conn
    def find_song(self, letters):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            condition = f'%{letters}%'
            sql = "SELECT * FROM songs WHERE title ILIKE %s ORDER BY title;"
            cur.execute(sql, (condition,))
            songsDAO = cur.fetchall()
            songs = []
            for DAO in songsDAO:
                song = Song(
                    title = DAO.title, 
                    artist_name = DAO.artist_name,
                    id = DAO.id
                    )
                songs.append(song)
            return songs
            #print('songs', songs)

# END