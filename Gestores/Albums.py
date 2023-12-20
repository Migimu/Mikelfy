from Clases.Album import Album
from Clases.Artist import Artist

class Albums:
    
    # __albums: [Album]
    
    def __init__(self, albums = []):
        self.__albums = albums
    
    def GET_ALBUMS(self):
        return self.__albums

    def GET_ALBUM_BY_NAME(self, name: str):
        encontrado = False
        cont = 0
        album = ""
        while cont < len(self.__albums) and not encontrado:
            if name == self.__albums[cont].GET_NAME():
                album = self.__albums[cont]
                encontrado = True
            cont+=1
        return album

    def GET_TOP_ALBUMS(self):
        self.__albums.sort(key=lambda album: album.GET_POPULARITY())
        return self.__albums

    # def GET_TOP_ALBUMS_BY_COUNTRY(self):
    #     return ""

    def GET_ALBUMS_BY_ARTIST(self, artis: Artist):
        artistAlbums = []
        for album in self.__albums:
            if album.GET_ARTIST().GET_ID() == artis.GET_ID():
                artistAlbums.append(album)
        
        return artistAlbums






