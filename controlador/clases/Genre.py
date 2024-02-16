class Genre:

    def __init__(self, id: int, name: str, isSubgenre: bool, popularity: int):
        self.__id = id
        self.__name = name
        self.__isSubgenre = isSubgenre
        self.__popularity = popularity
        self.__relatedGenres = []
        self.__parentGenres = []
    
    @property
    def id(self):
        return self.__id
    
    def GET_NAME(self):
        return self.__name
    
    def SET_NAME(self, name: str):
        self.__name = name
        
    def GET_IS_SUBGENRE(self):
        return self.__isSubgenre
    
    def CHANGE_IS_SUBGENRE(self):
        self.__isSubgenre = not self.__isSubgenre     
    
    def GET_POPULARITY(self):
        return self.__popularity
    
    def SET_POPULARITY(self, popularity: int):
        self.__popularity = popularity        



