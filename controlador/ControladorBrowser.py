from controlador.gestores.Artists import Artists
from controlador.gestores.Albums import Albums
from controlador.gestores.Songs import Songs
from controlador.gestores.Genres import Genres


class ControladorBrowser:
    
    def __init__(self):
        self.artists = Artists()
        self.albums = Albums()
        self.songs = Songs()
        self.genres = Genres()
        
    # def  SEARCH(self, word, isArtist = False, isAlbum = False, isSong = False, genre = None, startYear = None, endyear = None):
    #     return self.GET_ALL_COINCIDENCES(word)
      
    def GET_ALL_COINCIDENCES(self, word, showArtists = True, showAlbums = True, showSongs = True, genre = None, startYear = None, endyear = None):
        result = []
        if showArtists: result.extend(self.artists.GET_ARTISTS_BY_FILTER(word, genre))
        if showAlbums: result.extend(self.albums.GET_ALBUMS_BY_FILTER(word, startYear, endyear, genre))
        if showSongs: result.extend(self.songs.GET_SONGS_BY_FILTER(word, startYear, endyear, genre))
        
        return result
        
    # def GET_ALL_COINCIDENCES_BY_GENRE(self, word, genre):       
    #    pass
        
    # def GET_ALL_COINCIDENCES_BY_YEAR(self, word, year):       
    #     pass
        
    def GET_ALL_ARTISTS(self, genre = None):       
        return self.artists.GET_ARTISTS_BY_FILTER("", genre)
        
    # def GET_ALL_ARTISTS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_ARTISTS_BY_YEAR(self, username):       
    #     pass
        
    def GET_ALL_ALBUMS(self, genre = None, startYear = None, endyear = None):       
        self.albums.GET_ALBUMS_BY_FILTER("", startYear, endyear, genre)
        
    # def GET_ALL_ALBUMS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_ALBUMS_BY_YEAR(self, username):       
    #     pass
        
    def GET_ALL_SONGS(self, genre = None, startYear = None, endyear = None):       
        self.songs.GET_SONGS_BY_FILTER("", startYear, endyear, genre)
        
    # def GET_ALL_SONGS_BY_GENRE(self, username, password):       
    #     pass
        
    # def GET_ALL_SONGS_BY_YEAR(self, username):       
    #     pass
    
    def GET_ALL_GENRES(self):
        return self.genres.GET_GENRES()

        









