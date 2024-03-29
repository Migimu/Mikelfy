from assets.util.Utils import FIND, GET_LAST_ID
from modelo.LocalStorage import localStorage
from controlador.clases.Playlist import Playlist

class Playlists:
    
    def __init__(self, playlists = []):
        if len(playlists) == 0:
            self.__playlists = localStorage.playlists
        else:            
            self.__playlists = playlists                

    def GET_PLAYLISTS(self):
        return self.__playlists
       
    def GET_PLAYLIST_BY_ID(self, id):
        playlistEncontrado = FIND(self.__playlists, id = id)
        return playlistEncontrado

    def GET_PLAYLIST_BY_NAME(self, name):
        playlistEncontrado = FIND(self.__playlists, name = name)
        return playlistEncontrado

    def GET_PLAYLISTS_BY_USER(self, userId):
        userPlaylists = []
        for playlist in self.__playlists:
            if playlist.owner == userId:
                userPlaylists.append(playlist)
        
        return userPlaylists

    def GET_TOP_PLAYLISTS(self):
        sortedPlaylists = sorted(self.__playlists, key=lambda x: x.followers, reverse=True)       
        return sortedPlaylists[:5]

    def ADD_PLAYLIST(self, name:str, followers: int, userId: int):
        playlist = Playlist(GET_LAST_ID(self.__playlists), name, followers, userId)
        self.__playlists.append(playlist)
        localStorage.createdPlaylists = playlist

    def UPDATE_PLAYLIST(self, id: int, name:str, songsId = []):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__playlists):
            playlist: Playlist = self.__playlists[cont]
            if playlist.id == id:
                encontrado = True
                self.__playlists[cont].name = name
                self.__playlists[cont].songs = songsId
                localStorage.updatedPlaylists = self.__playlists[cont]
            cont += 1       

    def DELETE_PLAYLIST(self, id: int):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__playlists):
            playlist: Playlist = self.__playlists[cont]
            if playlist.id == id:
                encontrado = True
                localStorage.deletedPlaylists = self.__playlists[cont]
                self.__playlists.pop(cont)               
            cont += 1
        
    def DELETE_SONG_FROM_PLAYLIST(self,playlistId: int, songId: int):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__playlists):
            playlist: Playlist = self.__playlists[cont]
            if playlist.id == playlistId:
                encontrado = True
                self.__playlists[cont].REMOVE_SONG(songId)
                localStorage.updatedPlaylists = self.__playlists[cont]
            cont += 1
