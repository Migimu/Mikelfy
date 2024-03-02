class Artist:
    
    def __init__(self, id: int, name: str, country: str, followers: int, popularity: int, genreId: int):
        self.__id = id
        self.__name = name
        self.__country = country
        self.__followers = followers
        self.__popularity = popularity
        self.__genre = genreId
        self.__songs = []
        self.__albums = []
    
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
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, country: str):
        self.__country = country     
    
    @property
    def followers(self):
        return self.__followers
    
    @followers.setter
    def followers(self, followers: int):
        self.__followers = followers
    
    @property
    def popularity(self):
        return self.__popularity
    
    @popularity.setter
    def popularity(self, popularity: int):
        self.__popularity = popularity     
        
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
    def albums(self):
        return self.__albums
    
    @albums.setter
    def albums(self, albums):
        self.__albums = albums        





