from modelo.mockUsers import generos

class Genres:   

    def __init__(self, genres = []):
        if len(genres) == 0:
            self.__genres = generos
        else:            
            self.__genres = genres

    def GET_GENRES(self):
        return self.__genres

    def GET_GENRE_BY_NAME(self):
        return ""

    def GET_GENRES_BY_SONG(self):
        return []

    def GET_GENRES_BY_ARTIST(self):
        return []


