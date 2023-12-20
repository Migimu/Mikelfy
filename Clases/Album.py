from Clases.Artist import Artist
from Clases.Song import Song
from Gestores.Songs import Songs

class Album(Songs):
    
    # __id: int
    # __name: str
    # __popularity: int
    # __releaseYear: int
    # __isExplicit: bool
    # __isExplicit: Artist
    # __songs: Songs
    
    def __init__(self, id: int, name: str, popularity: int, releaseYear: int, isExplicit: bool, artistId: int):
        self.__id = id
        self.__name = name
        self.__popularity = popularity
        self.__releaseYear = releaseYear
        self.__isExplicit = isExplicit
        self.__artistId = artistId
        self.__songs = Songs.__init__(self)
    
    def GET_ID(self):
        return self.__id
    
    def GET_NAME(self):
        return self.__name
    
    def SET_NAME(self, name: str):
        self.__name = name
    
    def GET_POPULARITY(self):
        return self.__popularity
    
    def SET_POPULARITY(self, popularity: int):
        self.__popularity = popularity

    def GET_RELEASE_YEAR(self):
        return self.__releaseYear
    
    def SET_RELEASE_YEAR(self, releaseYear: int):
        self.__releaseYear = releaseYear
        
    def GET_IS_EXPLICIT(self):
        return self.__isExplicit
    
    def CHANGE_IS_EXPLICIT(self):
        self.__isExplicit = not self.__isExplicit

    def GET_SONGS(self):
        return self.__songs
    
    def SET_SONGS(self, songs: Songs):
        self.__songs = songs



