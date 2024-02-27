from modelo.mockUsers import listaDeReproduccion
from controlador.clases.Playlist import Playlist
from controlador.clases.User import User

class Playlists:
    
    def __init__(self, playlists = []):
        if len(playlists) == 0:
            self.__playlists = listaDeReproduccion
        else:            
            self.__playlists = playlists                

    def GET_PLAYLISTS(self):
        return self.__playlists

    def GET_PLAYLIST_BY_NAME(self):
        return ""
       
    def GET_PLAYLISTS_BY_USER(self, userId: User):
        userPlaylists = []
        for playlist in self.__playlists:
            if playlist.owner == userId:
                userPlaylists.append(playlist)
        
        return userPlaylists

    def GET_TOP_PLAYLISTS(self):
        return ""

    def GET_TOP_PLAYLISTS_BY_COUNTRY(self):
        return ""
    
    def GET_USER_PLAYLISTS(self):
        return True

    def ADD_PLAYLIST(self, name:str, followers: int, userId: int):
        playlist = Playlist(0, name, followers, userId)
        self.__playlists.append(playlist)
        # return playlist

    def UPDATE_PLAYLIST(self, playlist: Playlist):
        return True

    def DELETE_PLAYLIST(self, playlist: Playlist):
        return True



