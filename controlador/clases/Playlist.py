class Playlist:
    
    def __init__(self, id: int, name: str, followers: int, userId: int):
        self.__id = id
        self.__name = name
        self.__followers = followers
        self.__owner = userId
        self.__songs = []
    
    @property
    def id(self):
        return self.__id
    
    def GET_NAME(self):
        return self.__name
    
    def SET_NAME(self, name: str):
        self.__name = name
    
    def GET_POPULARITY(self):
        return self.__followers
    
    def SET_POPULARITY(self, followers: int):
        self.__followers = followers

    def GET_OWNER(self):
        return self.__owner       

    def GET_SONGS(self):
        return self.__songs
    
    def SET_SONGS(self, songs: [int]):
        self.__songs = songs




