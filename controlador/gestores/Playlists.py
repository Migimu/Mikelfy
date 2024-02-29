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
       
    def GET_PLAYLIST_BY_ID(self, id):
        encontrado = False
        playlistEncontrado = None
        cont = 0
        while not encontrado and cont < len(self.__playlists):
            playlist: Playlist = self.__playlists[cont]
            if playlist.id == id:
                encontrado = True
                playlistEncontrado = playlist
            cont += 1
        return playlistEncontrado

    def GET_PLAYLISTS_BY_USER(self, userId):
        userPlaylists = []
        for playlist in self.__playlists:
            if playlist.owner == userId:
                userPlaylists.append(playlist)
        
        return userPlaylists

    def GET_TOP_PLAYLISTS(self):
        return ""

    def GET_TOP_PLAYLISTS_BY_COUNTRY(self):
        return ""   

    def ADD_PLAYLIST(self, name:str, followers: int, userId: int):
        playlist = Playlist(self.GET_LAST_ID(), name, followers, userId)
        self.__playlists.append(playlist)
        listaDeReproduccion = self.__playlists

    def UPDATE_PLAYLIST(self, id: int, name:str, songsId = []):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__playlists):
            playlist: Playlist = self.__playlists[cont]
            if playlist.id == id:
                encontrado = True
                self.__playlists[cont].name = name
                self.__playlists[cont].songs = songsId
            cont += 1
        listaDeReproduccion = self.__playlists

    def DELETE_PLAYLIST(self, id: int):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__playlists):
            playlist: Playlist = self.__playlists[cont]
            if playlist.id == id:
                encontrado = True
                self.__playlists.pop(cont)
            cont += 1
        listaDeReproduccion = self.__playlists
        
    def DELETE_SONG_FROM_PLAYLIST(self,playlistId: int, songId: int):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__playlists):
            playlist: Playlist = self.__playlists[cont]
            if playlist.id == playlistId:
                encontrado = True
                self.__playlists[cont].REMOVE_SONG(songId)
            cont += 1
        listaDeReproduccion = self.__playlists

    def GET_LAST_ID(self):
        id = 0
        lenght = len(self.__playlists)
        if lenght == 0:
            id = 1
        else:
            id = int(self.__playlists[lenght - 1].id) + 1         
        return id


