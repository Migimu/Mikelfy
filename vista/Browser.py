from PySide6 import QtGui
from PySide6.QtWidgets import QCheckBox, QComboBox, QGridLayout, QHBoxLayout, QLineEdit, QLabel, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget
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

        layout.addWidget(QCheckBox("Artistas"), 0, 0)
        layout.addWidget(QCheckBox("Albumes"), 0, 1)
        layout.addWidget(QCheckBox("Canciones"), 0, 2)
        
        layout.addWidget(QLineEdit(), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)
        layout.addWidget(QComboBox(), 1, 2)            
        
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


    def BUSCAR(self):     
       searchResults = self.cl.SEARCH(self.searchbar.searchBarInput.text())
       results = QWidget()
       results.setFixedWidth(550)
       resultsLayout = QVBoxLayout()
       for item in searchResults:
           resultsLayout.addWidget(self.BUILD_CARD(item))
       results.setLayout(resultsLayout)
       self.scroll.setAlignment(Qt.AlignHCenter)
       self.scroll.setWidget(results)
       
    def TOGGLE_FILTER(self):
        if self.filter.isHidden():           
            self.filter.show()
        else:
            self.filter.hide()
           
    def BUILD_CARD(self, item):
       card = QWidget()
       card.setMinimumWidth(200)
       card.setFixedHeight(60)
       # card.setStyleSheet("border: 1px solid")
       cardLayout = QHBoxLayout()
       iconPath = ""
       if isinstance(item, Artist):
           iconPath = "artista"
       elif isinstance(item, Album):
           iconPath = "album"
       elif isinstance(item, Song):
           iconPath = "cancion"
       songButton = QPushButton()
       songButton.setIcon(QtGui.QIcon(absPath("imagenes/"+ iconPath +".png")))
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


