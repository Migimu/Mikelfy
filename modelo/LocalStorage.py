from modelo.mockUsers import usuarios, canciones, albumes, artistas, generos, paises, listaDeReproduccion

class LOCAL_STORAGE:
    def __init__(self):
        self.__users = usuarios
        self.__countries = paises
        self.__artists = artistas
        self.__albums = albumes
        self.__songs = canciones
        self.__playlists = listaDeReproduccion
        self.__genres = generos
        
    @property
    def users(self):
        return self.__users
    
    @users.setter
    def users(self, users):
        self.__users = users
        
    @property
    def countries(self):
        return self.__countries
    
    @countries.setter
    def countries(self, countries):
        self.__countries = countries
        
    @property
    def artists(self):
        return self.__artists
    
    @artists.setter
    def artists(self, artists):
        self.__artists = artists
        
    @property
    def albums(self):
        return self.__albums
    
    @albums.setter
    def albums(self, albums):
        self.__albums = albums
        
    @property
    def songs(self):
        return self.__songs
    
    @songs.setter
    def songs(self, songs):
        self.__songs = songs
        
    @property
    def playlists(self):
        return self.__playlists
    
    @playlists.setter
    def playlists(self, playlists):
        self.__playlists = playlists
        
    @property
    def genres(self):
        return self.__genres
    
    @genres.setter
    def genres(self, genres):
        self.__genres = genres
        
global localStorage
localStorage = LOCAL_STORAGE()




