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
        self.__createdUsers = []
        self.__updatedUsers = []
        self.__createdPlaylists = []
        self.__deletedPlaylists = []
        self.__updatedPlaylists = []
        
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
        
    @property
    def createdUsers(self):
        return self.__createdUsers
    
    @createdUsers.setter
    def createdUsers(self, createdUsers):
        self.__createdUsers.append(createdUsers)
        
    @property
    def updatedUsers(self):
        return self.__updatedUsers
    
    @updatedUsers.setter
    def updatedUsers(self, updatedUsers):
        self.__updatedUsers.append(updatedUsers)
        
    @property
    def createdPlaylists(self):
        return self.__createdPlaylists
    
    @createdPlaylists.setter
    def createdPlaylists(self, createdPlaylists):
        self.__createdPlaylists.append(createdPlaylists)
        
    @property
    def deletedPlaylists(self):
        return self.__deletedPlaylists
    
    @deletedPlaylists.setter
    def deletedPlaylists(self, deletedPlaylists):
        self.__deletedPlaylists.append(deletedPlaylists)
        
    @property
    def updatedPlaylists(self):
        return self.__updatedPlaylists
    
    @updatedPlaylists.setter
    def updatedPlaylists(self, updatedPlaylists):
        self.__updatedPlaylists.append(updatedPlaylists)
        
global localStorage
localStorage = LOCAL_STORAGE()




