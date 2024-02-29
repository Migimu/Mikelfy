from PySide6 import QtGui
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt,  Signal, Slot
from controlador.ControladorBrowser import ControladorBrowser

from controlador.clases.Artist import Artist
from controlador.clases.Album import Album
from controlador.clases.Song import Song
from vista.browser.Filter import Filter
from vista.browser.Searchbar import Searchbar
from vista.util.MediaPlayer import MediaPlayer
from vista.util.Utils import absPath      

class Browser(QWidget):
# class Browser(QMainWindow):
    closed = Signal()
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle("Buscador")
        self.user = user
        self.cl:ControladorBrowser = ControladorBrowser()
        self.searchText = ""
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QVBoxLayout()
        
        self.searchbar = Searchbar()
        self.searchbar.searchButton.clicked.connect(self.BUSCAR)
        self.searchbar.filterButton.clicked.connect(self.TOGGLE_FILTER)
        self.searchbar.backButton.clicked.connect(self.VOLVER)
        layout.addWidget(self.searchbar, 1)

        self.filter = Filter(self.cl.GET_ALL_GENRES())       
        self.filter.hide()
        layout.addWidget(self.filter, 1)
        
        self.scroll = QScrollArea()        
        self.scroll.setFixedWidth(600)
        self.scroll.setFixedHeight(400)        
        self.BUSCAR()
        layout.addWidget(self.scroll, 7, Qt.AlignCenter)
        

        self.mediaPlayer = MediaPlayer()
        self.mediaPlayer.setFixedWidth(600)
        layout.addWidget(self.mediaPlayer, 1, Qt.AlignCenter)

        layout.setSpacing(0)                                

        self.setLayout(layout)


    def BUSCAR(self, word = None):     
       inputWord = self.searchbar.searchBarInput.text()
       showArtists = self.filter.artistCheckbox.isChecked()
       showAlbums = self.filter.albumsCheckbox.isChecked()
       showSongs = self.filter.songsCheckbox.isChecked()
       startYear = self.filter.yearStartInput.value()
       endYear = self.filter.yearEndInput.value()
       genreId = self.filter.genreCombobox.currentData()
       searchResults = self.cl.GET_ALL_COINCIDENCES(inputWord if not word else word, showArtists, showAlbums, showSongs, genreId, startYear, endYear)
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
    
    def VOLVER(self):
       self.close() 
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)


