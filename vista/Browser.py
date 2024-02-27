from PySide6 import QtGui
from PySide6.QtWidgets import QCheckBox, QComboBox, QGridLayout, QHBoxLayout, QLineEdit, QLabel, QMainWindow, QPushButton, QScrollArea, QSpinBox, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt,  Signal, Slot
from controlador.ControladorBrowser import ControladorBrowser

from controlador.clases.Artist import Artist
from controlador.clases.Album import Album
from controlador.clases.Song import Song
from vista.mediaPlayer import MediaPlayer
from vista.utils import absPath

class Filter(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QGridLayout()

        self.artistCheckbox = QCheckBox("Artistas")
        self.artistCheckbox.setChecked(True)
        layout.addWidget(self.artistCheckbox, 0, 0)
        self.albumsCheckbox = QCheckBox("Albumes")
        self.albumsCheckbox.setChecked(True)
        layout.addWidget(self.albumsCheckbox, 0, 1)
        self.songsCheckbox = QCheckBox("Canciones")
        self.songsCheckbox.setChecked(True)
        layout.addWidget(self.songsCheckbox, 0, 2)
        
        self.yearStartInput = QSpinBox()
        self.yearStartInput.setMinimum(1900)
        self.yearStartInput.setMaximum(2024)
        layout.addWidget(self.yearStartInput, 1, 0)
        self.yearEndInput = QSpinBox()
        self.yearEndInput.setMinimum(1900)
        self.yearEndInput.setMaximum(2024)
        layout.addWidget(self.yearEndInput, 1, 1)
        self.genreCombobox = QComboBox()
        layout.addWidget(self.genreCombobox, 1, 2)            
        
        self.setLayout(layout)

class Searchbar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QHBoxLayout()

        self.searchBarInput = QLineEdit()
        self.searchBarInput.setFixedHeight(35)
        layout.addWidget(self.searchBarInput, 8)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QtGui.QIcon(absPath("imagenes/buscar.png")))
        self.searchButton.setFixedSize(QSize(30,30))
        layout.addWidget(self.searchButton, 1)
        
        self.filterButton = QPushButton()
        self.filterButton.setIcon(QtGui.QIcon(absPath("imagenes/filtrar.png")))
        self.filterButton.setFixedSize(QSize(30,30))
        layout.addWidget(self.filterButton, 1)                   
        
        self.setLayout(layout)
        


# class Browser(QWidget):
class Browser(QMainWindow):
    closed = Signal()
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.cl:ControladorBrowser = ControladorBrowser()
        self.searchText = ""
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QVBoxLayout()
        
        self.searchbar = Searchbar()
        self.searchbar.searchButton.clicked.connect(self.BUSCAR)
        self.searchbar.filterButton.clicked.connect(self.TOGGLE_FILTER)
        layout.addWidget(self.searchbar, 1)

        self.filter = Filter()
        self.filter.hide()
        layout.addWidget(self.filter, 1)
        
        self.scroll = QScrollArea()        
        self.scroll.setFixedWidth(600)
        self.scroll.setFixedHeight(400)        
        self.scroll.setAlignment(Qt.AlignCenter)        
        self.scroll.setWidget(QLabel("No hay nada"))
        layout.addWidget(self.scroll, 7, Qt.AlignCenter)
        

        self.mediaPlayer = MediaPlayer()
        self.mediaPlayer.setFixedWidth(600)
        layout.addWidget(self.mediaPlayer, 1, Qt.AlignCenter)

        layout.setSpacing(0)                         
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.show()


    def BUSCAR(self, word = None):     
       inputWord = self.searchbar.searchBarInput.text()
       showArtists = self.filter.artistCheckbox.isChecked()
       showAlbums = self.filter.albumsCheckbox.isChecked()
       showSongs = self.filter.songsCheckbox.isChecked()
       searchResults = self.cl.GET_ALL_COINCIDENCES(inputWord if not word else word, showArtists, showAlbums, showSongs)
       if len(searchResults) > 0:
            results = self.BUILD_RESULTS(searchResults)
            self.scroll.setAlignment(Qt.AlignHCenter)
       else:
           results = QLabel("No hay nada")
           self.scroll.setAlignment(Qt.AlignCenter)
       
       self.scroll.setWidget(results)
       
    def BUILD_RESULTS(self, searchResults):
       results = QWidget()
       results.setFixedWidth(550)
       resultsLayout = QVBoxLayout()
       for item in searchResults:
           widget = None
           if isinstance(item, Artist):
               widget = self.BUILD_ARTIST_CARD(item)
           elif isinstance(item, Album):
               widget = self.BUILD_ALBUM_CARD(item)
           elif isinstance(item, Song):
               widget = self.BUILD_SONG_CARD(item)
           resultsLayout.addWidget(widget)
       results.setLayout(resultsLayout)
       
       return results
       
    def TOGGLE_FILTER(self):
        if self.filter.isHidden():           
            self.filter.show()
        else:
            self.filter.hide()
           
    def BUILD_ARTIST_CARD(self, item):
       card = QWidget()
       card.setMinimumWidth(200)
       card.setFixedHeight(60)
       cardLayout = QHBoxLayout()
       iconButton = QPushButton()
       iconButton.setIcon(QtGui.QIcon(absPath("imagenes/artista.png")))
       iconButton.setIconSize(QSize(30, 30))
       iconButton.setFlat(True)
       iconButton.setEnabled(False)
       cardLayout.addWidget(iconButton, 1)
       artistNameButton = QPushButton(item.name)
       artistNameButton.setStyleSheet("text-align:left;")
       artistNameButton.setFixedWidth(520)
       artistNameButton.setFixedHeight(50)
       artistNameButton.clicked.connect(lambda: self.BUSCAR(item.name))
       artistNameButton.setFlat(True)
       cardLayout.addWidget(artistNameButton, 9)
       card.setLayout(cardLayout)
       
       return card 
    
    def BUILD_ALBUM_CARD(self, item):
       card = QWidget()
       card.setMinimumWidth(200)
       card.setFixedHeight(60)
       cardLayout = QHBoxLayout()
       iconButton = QPushButton()
       iconButton.setIcon(QtGui.QIcon(absPath("imagenes/album.png")))
       iconButton.setIconSize(QSize(30, 30))
       iconButton.setFlat(True)
       iconButton.setEnabled(False)
       cardLayout.addWidget(iconButton, 1)
       albumNameButton = QPushButton(item.name)
       albumNameButton.setStyleSheet("text-align:left;")
       albumNameButton.setFixedWidth(520)
       albumNameButton.setFixedHeight(50)
       albumNameButton.clicked.connect(lambda: self.BUSCAR(item.name))
       albumNameButton.setFlat(True)
       cardLayout.addWidget(albumNameButton, 9)
       card.setLayout(cardLayout)
       
       return card 
    
    def BUILD_SONG_CARD(self, item):
       card = QWidget()
       card.setMinimumWidth(200)
       card.setFixedHeight(60)
       cardLayout = QHBoxLayout()
       songButton = QPushButton()
       songButton.setIcon(QtGui.QIcon(absPath("imagenes/cancion.png")))
       songButton.setIconSize(QSize(30, 30))
       songButton.setFlat(True)
       songButton.setEnabled(False)
       cardLayout.addWidget(songButton, 1)
       cardLayout.addWidget(QLabel(item.name), 8)
       playButton = QPushButton()
       playButton.setFixedSize(50, 50)
       playButton.setIconSize(QSize(30, 30))
       playButton.setIcon(QtGui.QIcon(absPath("imagenes/play.png")))
       playButton.setFlat(True)
       cardLayout.addWidget(playButton, 1)
       card.setLayout(cardLayout)
       
       return card                   
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)


