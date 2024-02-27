from controlador.gestores.Artists import Artists
from controlador.gestores.Albums import Albums
from controlador.gestores.Songs import Songs


class ControladorBrowser:
    
    def __init__(self):
        self.artists = Artists()
        self.albums = Albums()
        self.songs = Songs()
        
    # def  SEARCH(self, word, isArtist = False, isAlbum = False, isSong = False, genre = None, startYear = None, endyear = None):
    #     return self.GET_ALL_COINCIDENCES(word)
      
    def GET_ALL_COINCIDENCES(self, word, showArtists = True, showAlbums = True, showSongs = True, genre = None, startYear = None, endyear = None):
        result = []
        if showArtists: result.extend(self.artists.GET_ARTISTS_BY_FILTER(word, genre, startYear, endyear))
        if showAlbums: result.extend(self.albums.GET_ALBUMS_BY_FILTER(word, genre, startYear, endyear))
        if showSongs: result.extend(self.songs.GET_SONGS_BY_FILTER(word, genre, startYear, endyear))
        
        return result
        
    # def GET_ALL_COINCIDENCES_BY_GENRE(self, word, genre):       
    #    pass
        
    # def GET_ALL_COINCIDENCES_BY_YEAR(self, word, year):       
    #     pass
        
    def GET_ALL_ARTISTS(self, word, genre = None, startYear = None, endyear = None):       
        return self.artists.GET_ARTISTS_BY_FILTER("", genre, startYear, endyear)
        
    # def GET_ALL_ARTISTS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_ARTISTS_BY_YEAR(self, username):       
    #     pass
        
    def GET_ALL_ALBUMS(self, username, password, word, genre = None, startYear = None, endyear = None):       
        self.albums.GET_ALBUMS_BY_FILTER("", genre, startYear, endyear)
        
    # def GET_ALL_ALBUMS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_ALBUMS_BY_YEAR(self, username):       
    #     pass
        
    def GET_ALL_SONGS(self, username, password, word, genre = None, startYear = None, endyear = None):       
        self.songs.GET_SONGS_BY_FILTER("", genre, startYear, endyear)
        
    # def GET_ALL_SONGS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_SONGS_BY_YEAR(self, username):       
    #     pass
        

        









