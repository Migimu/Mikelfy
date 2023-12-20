from Clases.Playlist import Playlist
from Clases.User import User

class Playlists:
    
    # __playlists: [Playlist]
    
    def __init__(self, playlists = []):
        self.__playlists = playlists

    def GET_PLAYLISTS(self):
        return self.__playlists

    def GET_PLAYLIST_BY_NAME(self):
        return ""
       
    def GET_PLAYLISTS_BY_USER(self, user: User):
        userPlaylists = []
        for playlist in self.__playlists:
            if playlist.GET_OWNER().GET_ID() == user.GET_ID():
                userPlaylists.append(playlist)
        
        return userPlaylists

    def GET_TOP_PLAYLISTS(self):
        return ""

    def GET_TOP_PLAYLISTS_BY_COUNTRY(self):
        return ""
    
    def GET_USER_PLAYLISTS(self):
        return True

    def CRATE_PLAYLIST(self, playlist: Playlist):
        return True

    def UPDATE_PLAYLIST(self, playlist: Playlist):
        return True

    def DELETE_PLAYLIST(self, playlist: Playlist):
        return True



