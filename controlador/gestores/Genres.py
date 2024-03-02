from assets.util.Utils import FIND
from modelo.mockUsers import generos

class Genres:   

    def __init__(self, genres = []):
        if len(genres) == 0:
            self.__genres = generos
        else:            
            self.__genres = genres

    def GET_GENRES(self):
        return self.__genres
    
    def GET_GENRE_BY_ID(self, id):
        genreEncontrado = FIND(self.__genres, id=id)
        return genreEncontrado

    def GET_GENRE_BY_NAME(self, name):
        genreEncontrado = FIND(self.__genres, name=name)
        return genreEncontrado



