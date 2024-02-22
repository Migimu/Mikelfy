from modelo.mockUsers import albumes

class Albums:
    
    def __init__(self, albums = []):
        if len(albums) == 0:
            self.__albums = albumes
        else:            
            self.__albums = albums
    
    def GET_ALBUMS(self):
        return self.__albums
    
    def GET_ALBUM_BY_ID(self, id: int):
        encontrado = False
        cont = 0
        album = ""
        while cont < len(self.__albums) and not encontrado:
            if id == self.__albums[cont].id:
                album = self.__albums[cont]
                encontrado = True
            cont+=1
        return album

    def GET_ALBUMS_BY_NAME(self, name: str):
        albums = []
        for album in self.__albums:
            if album.name == name:
                albums.append(album)
        return albums

    # def GET_TOP_ALBUMS(self):
    #     self.__albums.sort(key=lambda album: album.popularity)
    #     return self.__albums

    # def GET_TOP_ALBUMS_BY_COUNTRY(self):
    #     return ""

    # def GET_ALBUMS_BY_ARTIST(self, artistId):
    #     artistAlbums = []
    #     for album in self.__albums:
    #         if album.GET_ARTIST().id == artistId:
    #             artistAlbums.append(album)
        
    #     return artistAlbums






