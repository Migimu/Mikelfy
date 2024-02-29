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
        
    def GET_ALL_COINCIDENCES_BY_ARTISTS(self, idArtist):       
       result = []
       result.extend(self.albums.GET_ALBUMS_BY_ARTIST(idArtist))
       result.extend(self.songs.GET_SONGS_BY_ARTIST(idArtist))
        
       return result
        
    def GET_ALL_COINCIDENCES_BY_ALBUM(self, idAlbum):       
       result = []
       result.extend(self.artists.GET_ARTISTS_BY_ALBUM(idAlbum))
       result.extend(self.songs.GET_SONGS_BY_ALBUM(idAlbum))
        
       return result
        
    def GET_ALL_GENRES(self):
        return self.genres.GET_GENRES()

        









