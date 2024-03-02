from modelo.mockUsers import paises

class Countries:   

    def __init__(self, countries = []):
        if len(countries) == 0:
            self.__countries = paises
        else:            
            self.__countries = countries

    def GET_COUNTRIES(self):
        return self.__countries

    def GET_GENRE_BY_NAME(self):
        return ""

    def GET_GENRES_BY_SONG(self):
        return []

    def GET_GENRES_BY_ARTIST(self):
        return []


