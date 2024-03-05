from modelo.LocalStorage import localStorage
from assets.util.Utils import FILTER, FIND

class Albums:
    
    def __init__(self, albums = []):
        if len(albums) == 0:
            self.__albums = localStorage.albums
        else:            
            self.__albums = albums
    
    def GET_ALBUMS(self):
        return self.__albums
    
    def GET_ALBUM_BY_ID(self, id: int):
        album = FIND(self.__albums, id=id)
        return album

    def GET_ALBUMS_BY_NAME(self, name: str):
        albums = []
        for album in self.__albums:
            if album.name == name:
                albums.append(album)
        return albums
    
    def GET_ALBUMS_BY_FILTER(self, name: str, startYear: int, endYear: int, genre: int):
        albums = []
        for album in self.__albums:
            if FILTER(album, name, startYear, endYear, genre):
                albums.append(album)
        return albums

    def GET_ALBUMS_BY_ARTIST(self, artistId):
        albums = []
        for album in self.__albums:
            if artistId in album.artists:
                albums.append(album)
        
        return albums






