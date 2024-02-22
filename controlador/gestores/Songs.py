from modelo.mockUsers import canciones

class Songs:

    def __init__(self, songs = []):
        if len(songs) == 0:
            self.__songs = canciones
        else:            
            self.__songs = songs
    
    def GET_SONGS(self):
        return self.__songs

    def GET_SONG_BY_ID(self, id: int):
        encontrado = False
        cont = 0
        song = ""
        while cont < len(self.__songs) and not encontrado:
            if id == self.__songs[cont].id:
                song = self.__songs[cont]
                encontrado = True
            cont+=1
        return song

    def GET_ALBUMS_BY_NAME(self, name: str):
        songs = []
        for song in self.__songs:
            if song.name == name:
                songs.append(song)
        return songs




