class User:
    
    def __init__(self, id: int, user: str, name: str, email: str, password: str, country: str, birthDate: str):
        self.__id = id
        self.__user = user
        self.__name = name
        self.__email = email
        self.__password = password
        self.__country = country
        self.__birthDate = birthDate
        self.__favouriteSongs = []
        self.__followedAlbums = []
        self.__followedPlaylists = []
        self.__followedShows = []
        self.__followedArtists = []
        self.__preferedGenres = []
    
    def GET_ID(self):
        return self.__id

    def GET_USER(self):
        return self.__user

    def SET_USER(self, user: str):
        self.__user = user
    
    def GET_NAME(self):
        return self.__name
    
    def SET_NAME(self, name: str):
        self.__name = name
    
    def GET_EMAIL(self):
        return self.__email
    
    def SET_EMAIL(self, email: str):
        self.__email = email

    def GET_PASSWORD(self):
        return self.__password
    
    def SET_PASSWORD(self, password: str):
        self.__password = password
        
    def GET_COUNTRY(self):
        return self.__country
    
    def SET_COUNTRY(self, country: str):
        self.__country = country
        
    def GET_BIRTHDATE(self):
        return self.__birthDate
    
    def SET_BIRTHDATE(self, birthDate: str):
        self.__birthDate = birthDate
    
    def GET_FAVOURITE_SONGS(self):
        return self.__favouriteSongs

    def ADD_SONG_TO_FAVOURITE_SONGS(self, songId: int):
        self.__favouriteSongs.append(songId)

    def REMOVE_SONG_FROM_FAVOURITE_SONGS(self, songId: int):
        self.__favouriteSongs.remove(songId)

    def GET_FOLLOWED_ALBUMS(self):
        return self.__followedAlbums

    def FOLLOW_ALBUM(self, albumId: int):
        self.__followedAlbums.append(albumId)

    def UNFOLLOW_ALBUM(self, albumId: int):
        self.__followedAlbums.remove(albumId)

    def GET_FOLLOWED_PLAYLISTS(self):
        return self.__followedPlaylists

    def FOLLOW_PLAYLIST(self, playlistId: int):
        self.__followedPlaylists.append(playlistId)

    def UNFOLLOW_PLAYLIST(self, playlistId: int):
        self.__followedPlaylists.remove(playlistId)

    def GET_FAVOURITE_SHOWS(self):
        return self.__followedShows

    def ADD_SHOW_TO_FAVOURITE_SHOWS(self, showId: int):
        self.__followedShows.append(showId)

    def REMOVE_SHOW_FROM_FAVOURITE_SHOWS(self, showId: int):
        self.__followedShows.remove(showId) 
    
    def GET_FOLLOWED_ARTISTS(self):
        return self.__followedArtists

    def FOLLOW_ARTIST(self, artistId: int):
        self.__followedArtists.append(artistId)

    def UNFOLLOW_ARTIST(self, artistId: int):
        self.__followedArtists.append(artistId)
        
    def GET_PREFERED_GENRES(self):
        return self.__preferedGenres

    def ADD_GENRE_TO_PREFERED_GENRES(self, genreId: int):
        self.__preferedGenres.append(genreId)

    def REMOVE_GENRE_FROM_PREFERED_GENRES(self, genreId: int):
        self.__preferedGenres.remove(genreId)




