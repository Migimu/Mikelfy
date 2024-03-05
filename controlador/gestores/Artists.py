from modelo.LocalStorage import localStorage
from assets.util.Utils import FILTER_ARTIST, FIND

class Artists:
    
    def __init__(self, artists = []):
        if len(artists) == 0:
            self.__artists = localStorage.artists
        else:            
            self.__artists = artists
    
    def GET_ARTISTS(self):
        return self.__artists
    
    def GET_ARTIST_BY_ID(self, id: int):
        artist = FIND(self.__artists, id=id)
        return artist

    def GET_ARTISTS_BY_NAME(self, name: str):
        artists = []
        for artist in self.__artists:
            if artist.name == name:
                artists.append(artist)
        return artists
    
    def GET_ARTISTS_BY_FILTER(self, name: str, genre: int):
        artists = []
        for artist in self.__artists:
            if FILTER_ARTIST(artist, name, genre):
                artists.append(artist)
        return artists            

    def GET_ARTISTS_BY_ALBUM(self, albumId):
        artists = []
        for artist in self.__artists:
            if albumId in artist.albums:
                artists.append(artist)
        
        return artists




