from controlador.clases.Album import Album
from controlador.clases.Artist import Artist
from controlador.clases.Genre import Genre
from controlador.clases.Playlist import Playlist
from controlador.clases.Song import Song
from controlador.clases.User import User

  

global usuarios 
usuarios = [User(1, 'mikel', '1234', '1234', '1234', '1234', '1234'), 
            User(2, 'pepe', '1234', '1234', '1234', '1234', '1234'), 
            User(3, 'morlock', '1234', '1234', '1234', '1234', '1234')]

global countries 
countries = ["España", "Francia", "Portugal", "UK", "Irlanda", "Paises Bajos", "Andorra", "Italia", "Alemania", "USA"]

global artistas 
art1 = Artist(1, 'Nirvana', 'USA', 9000, 9000, 1)
art1.albums = [1]
art1.songs = [1, 2]
art2 = Artist(2, 'Queen', 'UK', 11000, 11000, 1)
art2.albums = [2]
art2.songs = [3, 4]
art3 = Artist(3, 'The Beatles', 'UK', 10000, 10000, 1)
art3.albums = [3]
art3.songs = [5, 6]
art4 = Artist(4, 'Steavie Wonder', 'USA', 8000, 8000, 4)
art4.albums = [4]
art4.songs = [7, 8]
art5 = Artist(5, 'Big Reel Fish', 'USA', 6000, 6000, 3)
art5.albums = [5]
art5.songs = [9, 10]
art6 = Artist(6, 'The Interrupters', 'USA', 7000, 7000, 3)
art6.albums = [6]
art6.songs = [11, 12]
art7 = Artist(7, 'Boney M.', 'Alemania', 8500, 8500, 2)
art7.albums = [3]
art7.songs = [13, 14]
artistas = [art1, art2, art3, art4, art5, art6, art7]

global albumes 
alb1 = Album(1, 'NirvanaAlbum', 180, 1985, False, 1)
alb1.albums = [1]
alb1.songs = [1, 2]
alb2 = Album(2, 'QueenAlbum', 180, 1980, False, 1)
alb2.albums = [2]
alb2.songs = [3, 4]
alb3 = Album(3, 'BeatlesAlbum', 180, 1970, False, 1)
alb3.albums = [3]
alb3.songs = [5, 6]
alb4 = Album(4, 'SteavieAlbum', 180, 1975, False, 4)
alb4.albums = [4]
alb4.songs = [7, 8]
alb5 = Album(5, 'FishAlbum', 180, 1990, False, 3)
alb5.albums = [5]
alb5.songs = [9, 10]
alb6 = Album(6, 'InterruptersAlbum', 180, 2010, False, 3)
alb6.albums = [6]
alb6.songs = [11, 12]
alb7 = Album(7, 'BoneyAlbum', 180, 1965, False, 2)
alb7.albums = [3]
alb7.songs = [13, 14]
albumes = [alb1, alb2, alb3, alb4, alb5, alb6, alb7]

global canciones 
canciones = [Song(1, 'Smell Like Teen Spirit', 180, 0, 1985, False, 0, 1), 
         Song(2, 'Come As You Are', 180, 0, 1985, False, 0, 1), 
         Song(3, 'Bohemina Rhapsody', 360, 0, 1980, False, 0, 1),
         Song(4, 'Another One Bites The Dust', 180, 0, 1980, False, 0, 1),
         Song(5, 'Lucy In The Sky With Diamonds', 180, 0, 1970, False, 0, 1),
         Song(6, 'Hey Jude', 180, 0, 1970, False, 0, 5),
         Song(7, 'Superstition', 180, 0, 1975, False, 0, 4),
         Song(8, 'Sir Duke', 180, 0, 1975, False, 0, 4),
         Song(9, 'Beer', 180, 0, 1990, False, 0, 3),
         Song(10, 'Take On Me', 180, 0, 1990, False, 0, 3),
         Song(11, 'She Got Arrested', 180, 0, 2010, False, 0, 3),
         Song(12, "She's Kerosene", 180, 0, 2010, False, 0, 3),
         Song(13, 'Rasputin', 180, 0, 1965, False, 0, 2),
         Song(14, 'Dady Cool', 180, 0, 1965, False, 0, 2)]

global listaDeReproduccion 
listaDeReproduccion = [Playlist(1, 'Rocklist', 10, 1), 
         Playlist(2, 'Discolist', 5, 1), 
         Playlist(3, 'Skalist', 7, 1)]
         
global generos 
generos = [Genre(1, 'Rock'), 
            Genre(2, 'Disco'), 
            Genre(3, 'Ska'),
            Genre(4, 'Funk'),
            Genre(5, 'Pop')]






