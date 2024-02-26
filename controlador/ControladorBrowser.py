from controlador.gestores.Artists import Artists
from controlador.gestores.Albums import Albums
from controlador.gestores.Songs import Songs


class ControladorBrowser:
    
    def __init__(self):
        self.artists = Artists()
        self.albums = Albums()
        self.songs = Songs()
        
    def SEARCH(self, word, isArtist = False, isAlbum = False, isSong = False, genre = None, startYear = None, endyear = None):
        return self.GET_ALL_COINCIDENCES(word)
      
    def GET_ALL_COINCIDENCES(self, word, genre = None, startYear = None, endyear = None):
        result = []
        artists = self.artists.GET_ARTISTS_BY_FILTER(word, genre, startYear, endyear)
        albums = self.albums.GET_ALBUMS_BY_FILTER(word, genre, startYear, endyear)
        songs = self.songs.GET_SONGS_BY_FILTER(word, genre, startYear, endyear)
        result.extend(artists)
        result.extend(albums)
        result.extend(songs)
        
        return result
        
    # def GET_ALL_COINCIDENCES_BY_GENRE(self, word, genre):       
    #    pass
        
    # def GET_ALL_COINCIDENCES_BY_YEAR(self, word, year):       
    #     pass
        
    def GET_ALL_ARTISTS(self, word, genre = None, startYear = None, endyear = None):       
        pass
        
    # def GET_ALL_ARTISTS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_ARTISTS_BY_YEAR(self, username):       
    #     pass
        
    def GET_ALL_ALBUMS(self, username, password, word, genre = None, startYear = None, endyear = None):       
        pass
        
    # def GET_ALL_ALBUMS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_ALBUMS_BY_YEAR(self, username):       
    #     pass
        
    def GET_ALL_SONGS(self, username, password, word, genre = None, startYear = None, endyear = None):       
        pass
        
    # def GET_ALL_SONGS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_SONGS_BY_YEAR(self, username):       
    #     pass
        

        









