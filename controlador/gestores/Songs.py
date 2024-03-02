from assets.util.Utils import FIND
from modelo.mockUsers import canciones
from assets.util.Utils import FILTER

class Songs:

    def __init__(self, songs = []):
        if len(songs) == 0:
            self.__songs = canciones
        else:            
            self.__songs = songs
    
    def GET_SONGS(self):
        return self.__songs

    def GET_SONG_BY_ID(self, id: int):
        song = FIND(self.__songs, id=id)
        return song

    def GET_SONGS_BY_NAME(self, name: str):
        songs = []
        for song in self.__songs:
            if song.name == name:
                songs.append(song)
        return songs

    def GET_SONGS_BY_FILTER(self, name: str, startYear: int, endYear: int, genre: int):
        songs = []
        for song in self.__songs:
            if FILTER(song, name, startYear, endYear, genre):
                songs.append(song)
        return songs

    def GET_SONGS_BY_ARTIST(self, artistId):
        songs = []
        for song in self.__songs:
            if artistId in song.artists:
                songs.append(song)
        return songs
    
    def GET_SONGS_BY_ALBUM(self, albumId):
        songs = []
        for song in self.__songs:
            if albumId in song.albums:
                songs.append(song)
        return songs

