from controlador.clases.Album import Album
from controlador.clases.Artist import Artist
from controlador.clases.Genre import Genre
from controlador.clases.Song import Song
from controlador.clases.User import User

  

global usuarios 
usuarios = [User(1, 'mikel', '1234', '1234', '1234', '1234', '1234'), 
            User(2, 'pepe', '1234', '1234', '1234', '1234', '1234'), 
            User(3, 'morlock', '1234', '1234', '1234', '1234', '1234')]

global countries 
countries = ["España", "Francia", "Portugal", "UK", "Irlanda", "Paises Bajos", "Andorra", "Italia", "Alemania", "USA"]

global artistas 
artistas = [Artist(1, 'Nirvana', 'USA', 9000, 9000), 
           Artist(2, 'Queen', 'UK', 11000, 11000), 
           Artist(3, 'The Beatles', 'UK', 10000, 10000), 
           Artist(4, 'Steavie Wonder', 'USA', 8000, 8000), 
           Artist(5, 'Big Reel Fish', 'USA', 6000, 6000), 
           Artist(6, 'The Interrupters', 'USA', 7000, 7000), 
           Artist(7, 'Boney M.', 'Alemania', 8500, 8500)]

global albumes 
albumes = [Album(1, 'NirvanaAlbum', 180, 0, False, 0), 
          Album(2, 'QueenAlbum', 180, 0, False, 0), 
          Album(3, 'BeatlesAlbum', 180, 0, False, 0), 
          Album(4, 'SteavieAlbum', 180, 0, False, 0), 
          Album(5, 'FishAlbum', 180, 0, False, 0), 
          Album(6, 'InterruptersAlbum', 180, 0, False, 0), 
          Album(7, 'BoneyAlbum', 180, 0, False, 0), 
            ]

global canciones 
canciones = [Song(1, 'Smell Like Teen Spirit', 180, 0, 0, False, 0), 
         Song(1, 'Come As You Are', 180, 0, 0, False, 0), 
         Song(1, 'Bohemina Rhapsody', 360, 0, 0, False, 0),
         Song(1, 'Another One Bites The Dust', 180, 0, 0, False, 0),
         Song(1, 'Lucy In The Sky With Diamonds', 180, 0, 0, False, 0),
         Song(1, 'Hey Jude', 180, 0, 0, False, 0),
         Song(1, 'Superstition', 180, 0, 0, False, 0),
         Song(1, 'Sir Duke', 180, 0, 0, False, 0),
         Song(1, 'Beer', 180, 0, 0, False, 0),
         Song(1, 'Take On Me', 180, 0, 0, False, 0),
         Song(1, 'She Got Arrested', 180, 0, 0, False, 0),
         Song(1, "She's Kerosene", 180, 0, 0, False, 0),
         Song(1, 'Rasputin', 180, 0, 0, False, 0),
         Song(1, 'Dady Cool', 180, 0, 0, False, 0)]

global generos 
generos = [Genre(1, 'Rock'), 
            Genre(2, 'Disco'), 
            Genre(3, 'Ska')]






