CREATE DATABASE Mikelfy;

USE Mikelfy;

--- CREATE ---

CREATE TABLE Country (
  id INT NOT NULL,
  nombre VARCHAR(50),
  PRIMARY KEY (id),
);

CREATE TABLE Genre (
  id INT NOT NULL,
  nombre VARCHAR(50),
  PRIMARY KEY (id)
);

CREATE TABLE Usuario (
  id INT NOT NULL,
  nombre VARCHAR(50),
  username VARCHAR(50),
  email VARCHAR(50),
  contrasenia VARCHAR(50),
  birthdate INT,
  countryId INT,
  PRIMARY KEY (id),
  CONSTRAINT country_user_idfk FOREIGN KEY (countryId) REFERENCES Country (id),
);

CREATE TABLE Song (
  id INT NOT NULL,
  title VARCHAR(50),
  duration INT,
  popularity INT,
  reproductions INT,
  releaseYear INT,
  isExplicit BIT,
  genreId INT,
  PRIMARY KEY (id),
  CONSTRAINT genre_song_idfk FOREIGN KEY (genreId) REFERENCES Genre (id)
);

CREATE TABLE Album (
  id INT NOT NULL,
  title VARCHAR(50),
  popularity INT,
  releaseYear INT,
  isExplicit BIT,
  genreId INT,
  PRIMARY KEY (id),
  CONSTRAINT genre_album_idfk FOREIGN KEY (genreId) REFERENCES Genre (id)
);

CREATE TABLE Artist (
  id INT NOT NULL,
  title VARCHAR(50),
  popularity INT,
  followers INT,
  countryId INT,
  genreId INT,
  PRIMARY KEY (id),
  CONSTRAINT country_artist_idfk FOREIGN KEY (countryId) REFERENCES Country (id),
  CONSTRAINT genre_artist_idfk FOREIGN KEY (genreId) REFERENCES Genre (id)
);

CREATE TABLE Playlist (
  id INT NOT NULL,
  nombre VARCHAR(50),
  followers INT,
  userId int,
  PRIMARY KEY (id),
  CONSTRAINT user_playlist_idfk FOREIGN KEY (userId) REFERENCES Usuario (id)
);

CREATE TABLE ListSongPlaylist (
  id INT NOT NULL,
  songId INT,
  playlistId INT,
  PRIMARY KEY (id),
  CONSTRAINT song_playlist_idfk FOREIGN KEY (songId) REFERENCES Song (id),
  CONSTRAINT playlist_song_idfk FOREIGN KEY (playlistId) REFERENCES Playlist (id)
);

CREATE TABLE ListSongArtist (
  id INT NOT NULL,
  songId INT,
  artistId INT,
  PRIMARY KEY (id),
  CONSTRAINT song_artist_idfk FOREIGN KEY (songId) REFERENCES Song (id),
  CONSTRAINT artist_song_idfk FOREIGN KEY (artistId) REFERENCES Artist (id)
);

CREATE TABLE ListSongAlbum (
  id INT NOT NULL,
  songId INT,
  albumId INT,
  PRIMARY KEY (id),
  CONSTRAINT song_album_idfk FOREIGN KEY (songId) REFERENCES Song (id),
  CONSTRAINT album_song_idfk FOREIGN KEY (albumId) REFERENCES Album (id)
);

CREATE TABLE ListAlbumArtist (
  id INT NOT NULL,
  albumId INT,
  artistId INT,
  PRIMARY KEY (id),
  CONSTRAINT album_artist_idfk FOREIGN KEY (albumId) REFERENCES Album (id),
  CONSTRAINT artist_album_idfk FOREIGN KEY (artistId) REFERENCES Artist (id)
);

--- LOAD ---

INSERT INTO Country(id, nombre) values 
(1, 'España'),
(2, 'Francia'),
(3, 'Portugal'),
(4, 'UK'),
(5, 'Irlanda'),
(6, 'Paises Bajos'),
(7, 'Andorra'),
(8, 'Italia'),
(9, 'Alemania'),
(10, 'USA');

INSERT INTO Genre(id, nombre) values 
(1, 'Rock'),
(2, 'Disco'),
(3, 'Ska'),
(4, 'Funk'),
(5, 'Pop');

INSERT INTO Usuario(id, nombre, username, email, contrasenia, birthdate, countryId) values 
(1, 'mikel', 'mikelo', 'mikel@gmail.com', '1234', 2000, 1), 
(2, 'pepe', 'pepelo', 'pepe@gmail.com', '1234', 1950, 1), 
(3, 'morlock', 'morlocklo', 'morlock@gmail.com', '1234', 1900, 2);

INSERT INTO Song(id, title, duration, popularity, reproductions, releaseYear, isExplicit, genreId) values 
(1, 'Smell Like Teen Spirit', 180, 0, 0, 1985, 0, 1),
(2, 'Come As You Are', 180, 0, 0, 1985, 0, 1), 
(3, 'Bohemina Rhapsody', 360, 0, 0, 1980, 0, 1),
(4, 'Another One Bites The Dust', 180, 0, 0, 1980, 0, 1),
(5, 'Lucy In The Sky With Diamonds', 180, 0, 0, 1970, 0, 1),
(6, 'Hey Jude', 180, 0, 0, 1970, 0, 5),
(7, 'Superstition', 180, 0, 0, 1975, 0, 4),
(8, 'Sir Duke', 180, 0, 0, 1975, 0, 4),
(9, 'Beer', 180, 0, 0, 1990, 0, 3),
(10, 'Take On Me', 180, 0, 0, 1990, 0, 3),
(11, 'She Got Arrested', 180, 0, 0, 2010, 0, 3),
(12, 'Shes Kerosene', 180, 0, 0, 2010, 0, 3),
(13, 'Rasputin', 180, 0, 0, 1965, 0, 2),
(14, 'Dady Cool', 180, 0, 0, 1965, 0, 2);

INSERT INTO Album(id, title, popularity, releaseYear, isExplicit, genreId) values 
(1, 'NirvanaAlbum', 180, 1985, 0, 1),
(2, 'QueenAlbum', 180, 1980, 0, 1),
(3, 'BeatlesAlbum', 180, 1970, 0, 1),
(4, 'SteavieAlbum', 180, 1975, 0, 4),
(5, 'FishAlbum', 180, 1990, 0, 3),
(6, 'InterruptersAlbum', 180, 2010, 0, 3),
(7, 'BoneyAlbum', 180, 1965, 0, 2);

INSERT INTO Artist(id, title, popularity, followers, countryId, genreId) values 
(1, 'Nirvana', 9000, 9000, 1, 1),
(2, 'Queen', 11000, 11000, 2, 1),
(3, 'The Beatles', 10000, 10000, 3, 1),
(4, 'Steavie Wonder', 8000, 8000, 4, 4),
(5, 'Big Reel Fish', 6000, 6000, 5, 3),
(6, 'The Interrupters', 7000, 7000, 6, 3),
(7, 'Boney M.', 8500, 8500, 7, 2);

INSERT INTO Playlist(id, nombre, followers, userId) values
(1, 'Rocklist', 10, 1),
(2, 'Discolist', 5, 1),
(3, 'Skalist', 7, 1);

INSERT INTO ListSongPlaylist(id, songId, playlistId) values
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 13, 2),
(7, 14, 2),
(8, 9, 3),
(9, 10, 3),
(10, 11, 3),
(11, 12, 3);

INSERT INTO ListSongArtist(id, songId, artistId) values 
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 2),
(5, 5, 3),
(6, 6, 3),
(7, 7, 4),
(8, 8, 4),
(9, 9, 5),
(10, 10, 5),
(11, 11, 6),
(12, 12, 6),
(13, 13, 7),
(14, 14, 7);

INSERT INTO ListSongAlbum(id, songId, albumId) values 
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 2),
(5, 5, 3),
(6, 6, 3),
(7, 7, 4),
(8, 8, 4),
(9, 9, 5),
(10, 10, 5),
(11, 11, 6),
(12, 12, 6),
(13, 13, 7),
(14, 14, 7);

INSERT INTO ListAlbumArtist(id, albumId, artistId) values 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7);