class Album:
    
    def __init__(self, id: int, name: str, popularity: int, releaseYear: int, isExplicit: bool, genreId: int):
        self.__id = id
        self.__name = name
        self.__popularity = popularity
        self.__releaseYear = releaseYear
        self.__isExplicit = isExplicit
        self.__genre = genreId
        self.__songs = []
        self.__artists = []
        
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
    
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
    def genre(self):
        return self.__genre
        
    @genre.setter
    def genre(self, genre):
        self.__genre = genre
    
    @property
    def songs(self):
        return self.__songs
    
    @songs.setter
    def songs(self, songs):
        self.__songs = songs
        
    @property
    def artists(self):
        return self.__artists
    
    @artists.setter
    def artists(self, artists):
        self.__artists = artists
        
    
    
    



