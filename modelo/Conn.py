import pyodbc
from controlador.clases.Country import Country
from controlador.clases.Album import Album
from controlador.clases.Artist import Artist
from controlador.clases.Genre import Genre
from controlador.clases.Playlist import Playlist
from controlador.clases.Song import Song
from controlador.clases.User import User
from modelo.LocalStorage import localStorage

class CONEXION:
    def __init__(self):
        try:  
            #Clase
            self.conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=INKAULA112;'
                            'Database=Mikelfy;'
                            'Trusted_Connection=yes;')
            #Casa
            # self.conn = pyodbc.connect('Driver={SQL Server};'
            #                 'Server=DESKTOP-D2DV5DS;'
            #                 'Database=Mikelfy;'
            #                 'Trusted_Connection=yes;')
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            
    def LOAD_DATA(self):
        localStorage.users = self.LOAD_USERS()
        localStorage.songs = self.LOAD_SONGS()
        localStorage.albums = self.LOAD_ALBUMS()
        localStorage.artists = self.LOAD_ARTISTS()
        localStorage.genres = self.LOAD_GENRES()
        localStorage.countries = self.LOAD_COUNTRIES()
        localStorage.playlists = self.LOAD_PLAYLISTS()      
            
    def LOAD_USERS(self):
        try:           
            listaUsuarios = []
            cursor = self.conn.cursor()     

            sql = "SELECT u.id, u.nombre, u.username, u.email, u.contrasenia, u.birthdate, u.countryId FROM Usuario AS u"

            cursor.execute(sql)

            for row in cursor:
                usu = User(row.id, row.nombre, row.username, row.email, row.contrasenia, row.countryId, row.birthdate)
            
                listaUsuarios.append(usu)
    
            cursor.close()
        
            return listaUsuarios
        except Exception as e:
            print(f"Error al recuperar los datos: {e}")       
    
    def LOAD_SONGS(self):
        try:           
            listaSongs = []
            cursor = self.conn.cursor()     

            sql = """ SELECT s.id, s.title, s.duration, s.popularity, s.releaseYear, s.isExplicit, s.reproductions, s.genreId, ar.artistId, al.albumId
                    FROM Song AS s
                    INNER JOIN ListSongArtist AS ar ON s.id = ar.songId
                    INNER JOIN ListSongAlbum AS al ON s.id = al.songId """

            cursor.execute(sql) 
            
            songsDict = {}
            for row in cursor:
                if row.id not in songsDict:
                    songsDict[row.id] = {
                        "song": Song(row.id, row.title, row.duration, row.popularity, row.releaseYear, row.isExplicit, row.reproductions, row.genreId),
                        "artists": [],
                        "albums": []
                    }
                if row.artistId not in songsDict[row.id]["artists"]:
                    songsDict[row.id]["artists"].append(row.artistId)    
                if row.albumId not in songsDict[row.id]["albums"]:
                    songsDict[row.id]["albums"].append(row.albumId)
                
            for song in songsDict.values():
                s = song["song"]
                s.artists = song["artists"]
                s.albums = song["albums"]
                listaSongs.append(s)
    
            cursor.close()
        
            return listaSongs
        except Exception as e:
            print(f"Error al recuperar los datos: {e}")        
    
    def LOAD_ALBUMS(self):
        try:           
            listaAlbums = []
            cursor = self.conn.cursor()     

            sql = """ SELECT a.id, a.title, a.popularity, a.releaseYear, a.isExplicit, a.genreId, ar.artistId, s.songId
                    FROM Album AS a
                    INNER JOIN ListAlbumArtist AS ar ON a.id = ar.albumId
                    INNER JOIN ListSongAlbum AS s ON a.id = s.albumId """

            cursor.execute(sql)
            
            albumsDict = {}
            for row in cursor:
                if row.id not in albumsDict:
                    albumsDict[row.id] = {
                        "album": Album(row.id, row.title, row.popularity, row.releaseYear, row.isExplicit, row.genreId),
                        "artists": [],
                        "songs": []
                    }
                if row.artistId not in albumsDict[row.id]["artists"]:
                    albumsDict[row.id]["artists"].append(row.artistId) 
                if row.songId not in albumsDict[row.id]["songs"]:
                    albumsDict[row.id]["songs"].append(row.songId)
                
            for album in albumsDict.values():
                al = album["album"]
                al.artists = album["artists"]
                al.songs = album["songs"]
                listaAlbums.append(al)
    
            cursor.close()
        
            return listaAlbums
        except Exception as e:
            print(f"Error al recuperar los datos: {e}")       
    
    def LOAD_ARTISTS(self):
        try:           
            listaArtists = []
            cursor = self.conn.cursor()            
            
            sql = """ SELECT a.id, a.title, a.popularity, a.followers, a.countryId, a.genreId, al.albumId, s.songId
                    FROM Artist AS a
                    INNER JOIN ListAlbumArtist AS al ON a.id = al.artistId
                    INNER JOIN ListSongArtist AS s ON a.id = s.artistId """

            cursor.execute(sql)  
            
            artistsDict = {}
            for row in cursor:
                if row.id not in artistsDict:
                    artistsDict[row.id] = {
                        "artist": Artist(row.id, row.title, row.popularity, row.followers, row.countryId, row.genreId),
                        "albums": [],
                        "songs": []
                    }
                if row.albumId not in artistsDict[row.id]["albums"]:
                    artistsDict[row.id]["albums"].append(row.albumId)   
                if row.songId not in artistsDict[row.id]["songs"]:
                    artistsDict[row.id]["songs"].append(row.songId)
                
            for artist in artistsDict.values():
                art = artist["artist"]
                art.albums = artist["albums"]
                art.songs = artist["songs"]
                listaArtists.append(art)
    
            cursor.close()
        
            return listaArtists
        except Exception as e:
            print(f"Error al recuperar los datos: {e}")         
    
    def LOAD_GENRES(self):
        try:           
            listaGenres = []
            cursor = self.conn.cursor()     

            sql = "SELECT g.id, g.nombre FROM Genre AS g"

            cursor.execute(sql)

            for row in cursor:
                gen = Genre(row.id, row.nombre)          
                listaGenres.append(gen)
    
            cursor.close()
        
            return listaGenres
        except Exception as e:
            print(f"Error al recuperar los datos: {e}")         
    
    def LOAD_COUNTRIES(self):
        try:           
            listaCountries = []
            cursor = self.conn.cursor()     

            sql = "SELECT c.id, c.nombre FROM Country AS c"

            cursor.execute(sql)

            for row in cursor:
                con = Country(row.id, row.nombre)            
                listaCountries.append(con)
    
            cursor.close()
        
            return listaCountries
        except Exception as e:
            print(f"Error al recuperar los datos: {e}")        
    
    def LOAD_PLAYLISTS(self):
        try:           
            listaPlaylists = []
            cursor = self.conn.cursor()      
            
            sql = """ SELECT p.id, p.nombre, p.followers, p.userId, s.songId
                    FROM Playlist AS p
                    LEFT JOIN ListSongPlaylist AS s ON p.id = s.playlistId"""
                    
            cursor.execute(sql)   
                    
            playlistDict = {}

            for row in cursor:
                if row.id not in playlistDict:
                    playlistDict[row.id] = Playlist(row.id, row.nombre, row.followers, row.userId)
                    
                if row.songId not in playlistDict[row.id].songs and row.songId != None:
                    playlistDict[row.id].ADD_SONG(row.songId)
                               
            listaPlaylists = list(playlistDict.values())        
    
            cursor.close()
        
            return listaPlaylists
        except Exception as e:
            print(f"Error al recuperar los datos: {e}") 
        
    def CREATE_USERS(self):        
        try:
            if len(localStorage.createdUsers) > 0:
                cursor = self.conn.cursor()
            
                sql = "INSERT INTO Usuario (id, nombre, username, email, contrasenia, birthdate, countryId) VALUES (?, ?, ?, ?, ?, ?, ?)"
                values=[]
                for newUser in localStorage.createdUsers:                
                    val = (newUser.id, newUser.name, newUser.username, newUser.email, newUser.password, newUser.birthDate, newUser.country)
                    values.append(val)
                cursor.executemany(sql, values)
                cursor.commit()
                print(cursor.rowcount, "record(s) affected")
                cursor.close()           
        except pyodbc.Error as e:
            print(f"Error de SQL al insetar los datos: {e}")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
             
            
    def UPDATE_USERS(self):
        try:
            if len(localStorage.updatedUsers) > 0:
                cursor = self.conn.cursor()     

                sql = "UPDATE Usuario SET nombre = ? , username = ?, email = ?, contrasenia = ?, birthdate = ?, countryId = ? WHERE id = ?"       
                values=[]
                for updatedUser in localStorage.updatedUsers:                
                    val = (updatedUser.name, updatedUser.username, updatedUser.email, updatedUser.password, updatedUser.birthDate, updatedUser.country, updatedUser.id)
                    values.append(val)
                cursor.executemany(sql, values)
                cursor.commit()
                print(cursor.rowcount, "record(s) affected")    
                cursor.close()
        except pyodbc.Error as e:
            print(f"Error de SQL al actualizar los datos: {e}")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            
    def CREATE_PLAYLISTS(self):        
        try:
            if len(localStorage.createdPlaylists) > 0:
                cursor = self.conn.cursor()
                sql = "SELECT MAX(id) AS id FROM ListSongPlaylist"
                cursor.execute(sql)
                idSP = None
                for row in cursor:
                    idSP = row.id + 1
                sqlPlaylist = "INSERT INTO Playlist (id, nombre, followers, userId) VALUES (?, ?, ?, ?)"
                sqlRelation = "INSERT INTO ListSongPlaylist Playlist (id, songId, playlistId) VALUES ( ?, ?, ?)"
                valuesPlaylist=[]
                valuesRelation=[]
                for newPlaylist in localStorage.createdPlaylists:                
                    val = (newPlaylist.id, newPlaylist.name, newPlaylist.followers, newPlaylist.owner)
                    valuesPlaylist.append(val)
                    for songId in newPlaylist.songs: 
                        valuesRelation.append((idSP, songId, newPlaylist.id))
                        idSP += 1
                cursor.executemany(sqlPlaylist, valuesPlaylist)
                if len(valuesRelation) > 0:
                    cursor.executemany(sqlRelation, valuesRelation)
                cursor.commit()
                print(cursor.rowcount, "record(s) affected")
                cursor.close()           
        except pyodbc.Error as e:
            print(f"Error de SQL al insetar los datos: {e}")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
             
            
    def UPDATE_PLAYLISTS(self):
        try:
            if len(localStorage.updatedPlaylists) > 0:
                cursor = self.conn.cursor()     
                sql = "SELECT MAX(id) AS id FROM ListSongPlaylist"
                cursor.execute(sql)
                idSP = None
                for row in cursor:
                    idSP = row.id + 1
                sqlPlaylist = "UPDATE Playlist SET nombre = ? , followers = ?, userId = ? WHERE id = ?"       
                sqlRelation = "INSERT INTO ListSongPlaylist (id, songId, playlistId) VALUES (?, ?, ?)"
                valuesPlaylist=[]
                valuesRelation=[]
                for updatedPlaylist in localStorage.updatedPlaylists:                
                    val = (updatedPlaylist.name, updatedPlaylist.followers, updatedPlaylist.owner, updatedPlaylist.id)
                    valuesPlaylist.append(val)
                    for songId in updatedPlaylist.songs: 
                        valuesRelation.append((idSP, songId, updatedPlaylist.id))
                        idSP += 1
                ids = ",".join(str(updatedPlaylist.id) for updatedPlaylist in localStorage.updatedPlaylists)
                sql = "DELETE FROM ListSongPlaylist WHERE id IN (" + ids + ")"       
                cursor.execute(sql) 
                cursor.executemany(sqlPlaylist, valuesPlaylist)                
                cursor.executemany(sqlRelation, valuesRelation)
                cursor.commit()
                print(cursor.rowcount, "record(s) affected")    
                cursor.close()
        except pyodbc.Error as e:
            print(f"Error de SQL al actualizar los datos: {e}")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            
    def DELETE_PLAYLISTS(self):
        try:
            if len(localStorage.deletedPlaylists) > 0:
                cursor = self.conn.cursor()
                ids = ",".join(str(deletedPlaylist.id) for deletedPlaylist in localStorage.deletedPlaylists)
                sql = "DELETE FROM ListSongPlaylist WHERE playlistId IN (" + ids + ")"
                cursor.execute(sql)
                sql = "DELETE FROM Playlist WHERE id IN (" + ids + ")"       
                cursor.execute(sql)                               
                cursor.commit()
                print(cursor.rowcount, "record(s) affected")    
                cursor.close()
        except pyodbc.Error as e:
            print(f"Error de SQL al eliminar los datos: {e}")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
    
        







