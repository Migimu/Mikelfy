from controlador.gestores.Playlists import Playlists


class ControladorPlaylist:
    
    def __init__(self):
        self.playlists = Playlists()
        
    def GET_USER_PLAYLISTS(self, userId):
        return self.playlists.GET_PLAYLISTS_BY_USER(userId)

    def CREATE_PLAYLISTS(self, name, userId, followers = 1):
        return self.playlists.ADD_PLAYLIST(name, followers, userId)


