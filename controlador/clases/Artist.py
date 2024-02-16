
class Artist:
    
    def __init__(self, id: int, name: str, country: str, followers: int, popularity: int):
        self.__id = id
        self.__name = name
        self.__country = country
        self.__followers = followers
        self.__popularity = popularity
        self.__songs = []
        self.__albums = []
    
    @property
    def id(self):
        return self.__id
    
    def GET_NAME(self):
        return self.__name
    
    def SET_NAME(self, name: str):
        self.__name = name
        
    def GET_COUNTRY(self):
        return self.__country
    
    def SET_COUNTRY(self, country: str):
        self.__country = country        
    
    def GET_FOLLOWERS(self):
        return self.__followers
    
    def SET_FOLLOWERS(self, followers: int):
        self.__followers = followers
    
    def GET_POPULARITY(self):
        return self.__popularity
    
    def SET_POPULARITY(self, popularity: int):
        self.__popularity = popularity        

    def GET_SONGS(self):
        return self.__songs
    
    def SET_SONGS(self, songs: Songs):
        self.__songs = songs
    
    def GET_ALBUMS(self):
        return self.__albums
    
    def SET_ALBUMS(self, albums: Albums):
        self.__albums = albums





