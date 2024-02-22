import sys
from PySide6 import QtGui
from PySide6.QtGui import QIcon, QImage
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QLabel, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt,  Signal, Slot
from controlador.ControladorBrowser import ControladorBrowser

from controlador.clases.Artist import Artist
from controlador.clases.Album import Album
from vista.utils import absPath


class Searchbar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QHBoxLayout()

        self.searchBarInput = QLineEdit()
        self.searchBarInput.setFixedHeight(35)
        layout.addWidget(QLineEdit(), 8)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QtGui.QIcon(absPath("imagenes/buscar.png")))
        self.searchButton.setFixedSize(QSize(30,30))
        layout.addWidget(self.searchButton, 1)
        
        filterButton = QPushButton()
        filterButton.setIcon(QtGui.QIcon(absPath("imagenes/filtrar.png")))
        filterButton.setFixedSize(QSize(30,30))
        layout.addWidget(filterButton, 1)

        # modificamos los márgenes
        # layout.setContentsMargins(0, 0, 0, 0)

        # # modificamos el espaciado
        # layout.setSpacing(0)                     
        
        self.setLayout(layout)

# class Browser(QWidget):
class Browser(QMainWindow):
    closed = Signal()
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.cl:ControladorBrowser = ControladorBrowser()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QVBoxLayout()
        self.searchbar = Searchbar()
        self.searchbar.searchButton.clicked.connect(self.BUSCAR)
        layout.addWidget(self.searchbar, 1)
        
        self.scroll = QScrollArea()
        
        self.scroll.setWidget(QLabel("No hay nada"))

        # test = QVBoxLayout()

        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test.addWidget(self.BUILD_CARD(None))
        # test1 = QWidget()
        # test1.setLayout(test)
        # self.scroll.setWidget(test1)

        layout.addWidget(self.scroll, 9, Qt.AlignCenter)

        # layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)                     
        
        # self.setLayout(layout)
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.show()


    def BUSCAR(self):     
       searchResults = self.cl.SEARCH()
       results = QWidget()
       resultsLayout = QVBoxLayout()
       for item in searchResults:
           resultsLayout.addWidget(self.BUILD_CARD(item))
       results.setLayout(resultsLayout)
       self.scroll.setWidget(results)
           
    def BUILD_CARD(self, item):
       card = QWidget()
       cardLayout = QHBoxLayout()
       iconPath = ""
       if isinstance(item, Artist):
           iconPath = "artista"
       elif isinstance(item, Album):
           iconPath = "album"
       else:
           iconPath = "cancion"
       songButton = QPushButton()
       songButton.setIcon(QtGui.QIcon(absPath("imagenes/"+ iconPath +".png")))
       songButton.setFlat(True)
       cardLayout.addWidget(songButton, 1)
       cardLayout.addWidget(QLabel("I wanna rock"), 3)
       cardLayout.addWidget(QPushButton("<"), 1)
       card.setLayout(cardLayout)
       
       return card
              
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Browser(None)
#     window.show()
#     sys.exit(app.exec())

