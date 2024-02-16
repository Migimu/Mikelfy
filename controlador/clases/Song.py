class Song:
    
    def __init__(self, id: int, name: str, duration: int, popularity: int, releaseYear: int, isExplicit: bool, reproductions: int):
        self.__id = id
        self.__name = name
        self.__duration = duration
        self.__popularity = popularity
        self.__releaseYear = releaseYear
        self.__isExplicit = isExplicit
        self.__reproductions = reproductions
    
    @property
    def id(self) -> int:
        return self.__id
    
    def GET_NAME(self):
        return self.__name
    
    def SET_NAME(self, name: str):
        self.__name = name
        
    def GET_DURATION(self):
        return self.__duration
    
    def SET_DURATION(self, duration: int):
        self.__duration = duration
    
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
        
    def GET_REPRODUCTIONS(self):
        return self.__reproductions
    
    def SET_REPRODUCTIONS(self, reproductions: int):
        self.__reproductions = reproductions

    def GET_ARTISTS(self):
        return self.__artists
    
    def SET_ARTISTS(self, artists: Artists):
        self.__artists = artists




