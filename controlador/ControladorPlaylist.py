from controlador.gestores.Playlists import Playlists
from controlador.gestores.Songs import Songs


class ControladorPlaylist:
    
    def __init__(self):
        self.playlists = Playlists()
        self.songs = Songs()
        
    def GET_SONGS(self):
        return self.songs.GET_SONGS()
        
    def GET_SONGS_BY_ID(self, songsIds):
        songs = []
        for songId in songsIds:
            songs.append(self.songs.GET_SONG_BY_ID(songId))
        return songs

    def GET_USER_PLAYLISTS(self, userId):
        return self.playlists.GET_PLAYLISTS_BY_USER(userId)

    def CREATE_PLAYLISTS(self, name, userId, followers = 1):
        self.playlists.ADD_PLAYLIST(name, followers, userId)
    
    def DELETE_PLAYLISTS(self, playlistId):
        self.playlists.DELETE_PLAYLIST(playlistId)
        
    def DELETE_SONG_FROM_PLAYLIST(self, playlistId, songId):
        self.playlists.DELETE_SONG_FROM_PLAYLIST(playlistId, songId)
    
    def UPDATE_PLAYLISTS(self, playlistId, name):
        self.playlists.UPDATE_PLAYLIST(playlistId, name)


