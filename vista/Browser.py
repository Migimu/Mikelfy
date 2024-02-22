from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt,  Signal, Slot
from controlador.ControladorBrowser import ControladorBrowser

from controlador.clases.Artist import Artist
from controlador.clases.Album import Album

class Searchbar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QHBoxLayout()

        searchBarInput = QLineEdit()
        searchBarInput.setFixedHeight(35)
        layout.addWidget(QLineEdit(), 8)

        searchButton = QPushButton()
        searchButton.setFixedSize(QSize(30,30))
        layout.addWidget(searchButton, 1)
        
        filterButton = QPushButton()
        filterButton.setFixedSize(QSize(30,30))
        layout.addWidget(filterButton, 1)

        # modificamos los márgenes
        # layout.setContentsMargins(0, 0, 0, 0)

        # # modificamos el espaciado
        # layout.setSpacing(0)                     
        
        self.setLayout(layout)

class Browser(QWidget):
    closed = Signal()
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.cl:ControladorBrowser = ControladorBrowser()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QVBoxLayout()

        layout.addWidget(Searchbar(), 1)
        
        self.scroll = QScrollArea()
        self.scroll.setWidget(QLabel("No hay nada"))
        layout.addWidget(self.scroll, 9, Qt.AlignHCenter)

        # layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)                     
        
        self.setLayout(layout)


    def BUSCAR(self):      
       searchResults = self.cl.GET_ALL_COINCIDENCES_BY_GENRE()
       results = QVBoxLayout()
       for item in searchResults:
           results.addWidget(self.BUILD_CARD(item))
       self.scroll.setWidget(results)
           
    def BUILD_CARD(self, item):
       card = QHBoxLayout()
       iconPath = ""
       if isinstance(item, Artist):
           iconPath = "artist"
       elif isinstance(item, Album):
           iconPath = "album"
       else:
           iconPath = "song"
       card.addWidget(QLabel(QIcon(iconPath)), 1)
       card.addWidget(QLabel(""), 3)
       card.addWidget(QPushButton("<"), 1)
       
       return card
              
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)


