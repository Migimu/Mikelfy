from assets.util.Utils import FIND
from modelo.mockUsers import paises

class Countries:   

    def __init__(self, countries = []):
        if len(countries) == 0:
            self.__countries = paises
        else:            
            self.__countries = countries

    def GET_COUNTRIES(self):
        return self.__countries
    
    def GET_COUNTRY_BY_ID(self, id):
        countryEncontrado = FIND(self.__countries ,id=id)
        return countryEncontrado

    def GET_COUNTRY_BY_NAME(self, name):
        countryEncontrado = FIND(self.__countries ,name=name)
        return countryEncontrado



