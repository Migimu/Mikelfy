from Clases.User import User
from Gestores.Songs import Songs


class Playlist(Songs):
    # __id: str
    # __name:str
    # __followers: int
    # __owner: User
    # __songs: Songs
    
    def __init__(self, id: int, name: str, followers: int, userId: int):
        self.__id = id
        self.__name = name
        self.__followers = followers
        self.__owner = userId
        self.__songs = Songs.__init__(self)
    
    def GET_ID(self):
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
    
    def SET_SONGS(self, songs: Songs):
        self.__songs = songs




