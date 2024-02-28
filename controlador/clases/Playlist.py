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
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
    
    @property
    def followers(self):
        return self.__followers
    
    @followers.setter
    def followers(self, followers: int):
        self.__followers = followers

    @property
    def owner(self):
        return self.__owner       

    @property
    def songs(self):
        return self.__songs
    
    @songs.setter
    def songs(self, songs):
        self.__songs = songs
        
    def ADD_SONG(self, songId: int):
        self.__favouriteSongs.append(songId)

    def REMOVE_SONG(self, songId: int):
        self.__favouriteSongs.remove(songId)




