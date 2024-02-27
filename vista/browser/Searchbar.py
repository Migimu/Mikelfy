from PySide6 import QtGui
from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QPushButton, QWidget
from PySide6.QtCore import QSize

from vista.util.Utils import absPath

class Searchbar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QHBoxLayout()
        
        self.backButton = QPushButton()
        self.backButton.setIcon(QtGui.QIcon(absPath("imagenes/back.png")))
        self.backButton.setFixedSize(QSize(30,30))
        layout.addWidget(self.backButton, 1)

        self.searchBarInput = QLineEdit()
        self.searchBarInput.setFixedHeight(35)
        layout.addWidget(self.searchBarInput, 7)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QtGui.QIcon(absPath("imagenes/buscar.png")))
        self.searchButton.setFixedSize(QSize(30,30))
        layout.addWidget(self.searchButton, 1)
        
        self.filterButton = QPushButton()
        self.filterButton.setIcon(QtGui.QIcon(absPath("imagenes/filtrar.png")))
        self.filterButton.setFixedSize(QSize(30,30))
        layout.addWidget(self.filterButton, 1)                   
        
        self.setLayout(layout)




