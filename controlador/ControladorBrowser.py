from controlador.gestores.Artists import Artists
from controlador.gestores.Albums import Albums
from controlador.gestores.Songs import Songs


class ControladorBrowser:
    
    def __init__(self):
        self.artists = Artists()
        self.albums = Albums()
        self.songs = Songs()
      
    def GET_ALL_COINCIDENCES(self, word):       
        artists = self.artists.GET_ARTIST_BY_NAME(word)
        albums = self.albums.GET_ALBUM_BY_NAME(word)
        songs = self.songs.GET_SONG_BY_NAME(word)
        
        return artists, albums, songs
        
    def GET_ALL_COINCIDENCES_BY_GENRE(self, word, genre):       
       pass
        
    def GET_ALL_COINCIDENCES_BY_YEAR(self, word, year):       
        pass
        
    def GET_ALL_ARTISTS(self):       
        pass
        
    def GET_ALL_ARTISTS_BY_GENRE(self, username, password):       
        pass
        
    def GET_ALL_ARTISTS_BY_YEAR(self, username):       
        pass
        
    def GET_ALL_ALBUMS(self, username, password):       
        pass
        
    def GET_ALL_ALBUMS_BY_GENRE(self, username, password):       
        pass
        
    def GET_ALL_ALBUMS_BY_YEAR(self, username):       
        pass
        
    def GET_ALL_SONGS(self, username, password):       
        pass
        
    def GET_ALL_SONGS_BY_GENRE(self, username, password):       
        pass
        
    def GET_ALL_SONGS_BY_YEAR(self, username):       
        pass
        

        









