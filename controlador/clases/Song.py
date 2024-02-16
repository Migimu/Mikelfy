class Song:
    
    def __init__(self, id: int, name: str, duration: int, popularity: int, releaseYear: int, isExplicit: bool, reproductions: int):
        self.__id = id
        self.__name = name
        self.__duration = duration
        self.__popularity = popularity
        self.__releaseYear = releaseYear
        self.__isExplicit = isExplicit
        self.__reproductions = reproductions
        self.__albums = []
        self.__genres = []
        self.__artists = []
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
      
    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration
    
    @property
    def popularity(self):
        return self.__popularity
    
    @popularity.setter
    def popularity(self, popularity: int):
        self.__popularity = popularity

    @property
    def releaseYear(self):
        return self.__releaseYear
    
    @releaseYear.setter
    def releaseYear(self, releaseYear: int):
        self.__releaseYear = releaseYear
        
    @property
    def isExplicit(self):
        return self.__isExplicit
    
    @isExplicit.setter
    def isExplicit(self):
        self.__isExplicit = not self.__isExplicit
        
    @property
    def reproductions(self):
        return self.__reproductions
    
    @reproductions.setter
    def reproductions(self, reproductions: int):
        self.__reproductions = reproductions
        
    @property
    def albums(self):
        return self.__albums
    
    @albums.setter
    def albums(self, albums):
        self.__albums = albums
        
    @property
    def genres(self):
        return self.__genres
    
    @genres.setter
    def genres(self, genres):
        self.__genres = genres

    @property
    def artists(self):
        return self.__artists
    
    @artists.setter
    def artists(self, artists):
        self.__artists = artists




