import pyodbc
from controlador.clases.Album import Album
from controlador.clases.Artist import Artist
from controlador.clases.Genre import Genre
from controlador.clases.Playlist import Playlist
from controlador.clases.Song import Song
from controlador.clases.User import User


class CONEXION:
    def __init__(self):
        try:
            self.conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=INKAULA112;'
                            'Database=Mikelfy;'
                            'Trusted_Connection=yes;')
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            
    def LOAD_DATA(self):
        usuarios = self.LOAD_USERS()
        canciones = self.LOAD_SONGS()
        albumes = self.LOAD_ALBUMS()
        artistas = self.LOAD_ARTISTS()
        generos = self.LOAD_GENRES()
        countries = self.LOAD_COUNTRIES()                    
        listaDeReproduccion = self.LOAD_PLAYLISTS()
        
            
    def LOAD_USERS(self):
        
        listaUsuarios = []
        cursor = self.conn.cursor()     

        sql = "SELECT u.id, u.nombre, u.username, u.email, u.contrasenia, u.birthdate, u.countryId FROM Usuario AS u"

        cursor.execute(sql)

        for row in cursor:
            usu = User(row.id, row.nombre, row.username, row.email, row.contrasenia, row.countryId, row.birthdate)
            
            listaUsuarios.append(usu)
    
        cursor.close()
        
        return listaUsuarios
    
    def LOAD_SONGS(self):
        
        listaSongs = []
        cursor = self.conn.cursor()     

        sql = "SELECT s.id, s.title, s.duration, s.popularity, s.reproductions, s.releaseYear, s.isExplicit, s.genreId FROM Song AS s"

        cursor.execute(sql)

        for row in cursor:
            song = Song(row.id, row.title, row.duration, row.popularity, row.releaseYear, row.isExplicit, row.reproductions, row.genreId)           
            listaSongs.append(song)
    
        cursor.close()
        
        return listaSongs
    
    def LOAD_ALBUMS(self):
        
        listaUsuarios = []
        cursor = self.conn.cursor()     

        sql = "SELECT u.id, u.nombre, u.apellido1, u.apellido2, u.direccion, u.codigo_postal, u.email, p.pasword, an.anio_nacimiento FROM Usuario AS u, Passwords AS p, AnosNacimiento AS an WHERE u.id = p.usuario_id AND u.id = an.usuario_id"

        cursor.execute(sql)

        for row in cursor:
            usu = [row.id, row.nombre, row.apellido1, row.apellido2, row.direcion, row.cp, row.email]
            
            listaUsuarios.append(usu)
    
        cursor.close()
        
        return listaUsuarios
    
    def LOAD_ARTISTS(self):
        
        listaUsuarios = []
        cursor = self.conn.cursor()     

        sql = "SELECT u.id, u.nombre, u.apellido1, u.apellido2, u.direccion, u.codigo_postal, u.email, p.pasword, an.anio_nacimiento FROM Usuario AS u, Passwords AS p, AnosNacimiento AS an WHERE u.id = p.usuario_id AND u.id = an.usuario_id"

        cursor.execute(sql)

        for row in cursor:
            usu = [row.id, row.nombre, row.apellido1, row.apellido2, row.direcion, row.cp, row.email]
            
            listaUsuarios.append(usu)
    
        cursor.close()
        
        return listaUsuarios
    
    def LOAD_GENRES(self):
        
        listaUsuarios = []
        cursor = self.conn.cursor()     

        sql = "SELECT u.id, u.nombre, u.apellido1, u.apellido2, u.direccion, u.codigo_postal, u.email, p.pasword, an.anio_nacimiento FROM Usuario AS u, Passwords AS p, AnosNacimiento AS an WHERE u.id = p.usuario_id AND u.id = an.usuario_id"

        cursor.execute(sql)

        for row in cursor:
            usu = [row.id, row.nombre, row.apellido1, row.apellido2, row.direcion, row.cp, row.email]
            
            listaUsuarios.append(usu)
    
        cursor.close()
        
        return listaUsuarios
    
    def LOAD_COUNTRIES(self):
        
        listaUsuarios = []
        cursor = self.conn.cursor()     

        sql = "SELECT u.id, u.nombre, u.apellido1, u.apellido2, u.direccion, u.codigo_postal, u.email, p.pasword, an.anio_nacimiento FROM Usuario AS u, Passwords AS p, AnosNacimiento AS an WHERE u.id = p.usuario_id AND u.id = an.usuario_id"

        cursor.execute(sql)

        for row in cursor:
            usu = [row.id, row.nombre, row.apellido1, row.apellido2, row.direcion, row.cp, row.email]
            
            listaUsuarios.append(usu)
    
        cursor.close()
        
        return listaUsuarios
    
    def LOAD_PLAYLISTS(self):
        
        listaUsuarios = []
        cursor = self.conn.cursor()     

        sql = "SELECT u.id, u.nombre, u.apellido1, u.apellido2, u.direccion, u.codigo_postal, u.email, p.pasword, an.anio_nacimiento FROM Usuario AS u, Passwords AS p, AnosNacimiento AS an WHERE u.id = p.usuario_id AND u.id = an.usuario_id"

        cursor.execute(sql)

        for row in cursor:
            usu = [row.id, row.nombre, row.apellido1, row.apellido2, row.direcion, row.cp, row.email]
            
            listaUsuarios.append(usu)
    
        cursor.close()
        
        return listaUsuarios
    
    
    

    

    
    
    # def UPDATE(self, id, nombre, apellido1, apellido2, direcion, cp, email, anioNacimiento):
    #     cursor = self.conn.cursor()     

    #     sql = "UPDATE Usuario SET nombre = ? , apellido1 = ?, apellido2 = ?, direcion = ?, cp = ?, email = ? WHERE id = ?"
        
    #     val = (nombre, apellido1, apellido2, direcion, cp, email, int(id))

    #     cursor.execute(sql, val)
        
    #     sql = "UPDATE AnosNacimiento SET anio_nacimiento = ? WHERE usuario_id = ?"
        
    #     val = (nombre, apellido1, apellido2, direcion, cp, email, int(id))

    #     cursor.execute(sql, val)

    #     self.conn.commit()

    #     print(cursor.rowcount, "record(s) affected")
    
    #     cursor.close()
    
    # def DELETE(self, id):
    #     cursor = self.conn.cursor()     

    #     sql = "DELETE FROM Usuario WHERE id = ?"
        
    #     val = (id)

    #     cursor.execute(sql, val)

    #     self.conn.commit()

    #     print(cursor.rowcount, "record(s) affected")
    
    #     cursor.close()
    
    # def INSERT(self, nombre, apellido1, apellido2, direcion, cp, email, anioNacimiento, password):
        
    #     try:
    #         cursor = self.conn.cursor()
        
    #         val = (nombre, apellido1, apellido2, direcion, cp, email)
        
    #         cursor.execute(sql, val)
        
    #     except pyodbc.Error as e:
    #         print(f"Error de SQL al cargar libros desde la base de datos: {e}")
    #     except Exception as e:
    #         print(f"Error al cargar libros desde la base de datos: {e}")
             
    #     cursor = self.conn.cursor()     

    #     sql = "INSERT INTO Usuario (id, nombre, apellido1, apellido2, direcion, cp, email) VALUES ((SELECT MAX(id) FROM Usuario) + 1, ?, ?, ?, ?, ?, ?)"
        
    #     val = (nombre, apellido1, apellido2, direcion, cp, email)
        
    #     cursor.execute(sql, val)
        
    #     sql = "INSERT INTO AnosNacimiento (id, anio_nacimiento, usuario_id) VALUES ((SELECT MAX(id) FROM AnosNacimiento) + 1, ?, ?)"
        
    #     val = (anioNacimiento, int(id))

    #     cursor.execute(sql, val)
        
    #     sql = "INSERT INTO Passwords (id, password, usuario_id) VALUES ((SELECT MAX(id) FROM AnosNacimiento) + 1, ?, ?)"
        
    #     val = (password )

    #     cursor.execute(sql, val)



    #     self.conn.commit()

    #     print(cursor.rowcount, "record(s) affected")
    
    #     cursor.close()
        







