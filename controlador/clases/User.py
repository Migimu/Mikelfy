class User:
    def __init__(self, id: int, username: str, name: str, email: str, password: str, country: str, birthDate: str):
        self.__id = id
        self.__username = username
        self.__name = name
        self.__email = email
        self.__password = password
        self.__country = country
        self.__birthDate = birthDate
        self.__favouriteSongs = []
        self.__followedPlaylists = []
        
    def __str__(self):
        return self.__id ,'.- ', self.__username  
    
    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username: str):
        self.__username = username
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password: str):
        self.__password = password         
        
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, country: str):
        self.__country = country
        
    @property
    def birthDate(self):
        return self.__birthDate
    
    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate
    
    @property
    def favouriteSongs(self):
        return self.__favouriteSongs
    
    @favouriteSongs.setter
    def favouriteSongs(self, favouriteSongs):
        self.__favouriteSongs = favouriteSongs

    def ADD_FAVOURITE_SONGS(self, songId: int):
        self.__favouriteSongs.append(songId)

    def REMOVE_FROM_FAVOURITE_SONGS(self, songId: int):
        self.__favouriteSongs.remove(songId)

    @property
    def followedPlaylists(self):
        return self.__followedPlaylists
    
    @followedPlaylists.setter
    def followedPlaylists(self, followedPlaylists):
        self.__followedPlaylists = followedPlaylists

    def FOLLOW_PLAYLIST(self, playlistId: int):
        self.__followedPlaylists.append(playlistId)

    def UNFOLLOW_PLAYLIST(self, playlistId: int):
        self.__followedPlaylists.remove(playlistId) 


