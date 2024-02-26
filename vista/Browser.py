import sys
from PySide6 import QtGui
from PySide6.QtGui import QIcon, QImage
from PySide6.QtWidgets import QApplication, QCheckBox, QComboBox, QGridLayout, QHBoxLayout, QLineEdit, QLabel, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt,  Signal, Slot
from controlador.ControladorBrowser import ControladorBrowser

from controlador.clases.Artist import Artist
from controlador.clases.Album import Album
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
        self.scroll.setFixedWidth(200)
        self.scroll.setFixedHeight(400)        
        self.scroll.setWidget(QLabel("No hay nada"))
        layout.addWidget(self.scroll, 8, Qt.AlignCenter)

        layout.setSpacing(0)                         
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.show()


    def BUSCAR(self):     
       searchResults = self.cl.SEARCH(self.searchbar.searchBarInput.text())
       results = QWidget()
       resultsLayout = QVBoxLayout()
       for item in searchResults:
           resultsLayout.addWidget(self.BUILD_CARD(item))
       results.setLayout(resultsLayout)
       self.scroll.setWidget(results)
       
    def TOGGLE_FILTER(self):
        if self.filter.isHidden():           
            self.filter.show()
        else:
            self.filter.hide()
           
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

