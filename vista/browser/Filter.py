from PySide6 import QtGui
from PySide6.QtWidgets import QCheckBox, QComboBox, QGridLayout, QPushButton, QSpinBox, QWidget
from PySide6.QtCore import QSize

from vista.util.Utils import absPath

class Filter(QWidget):
    def __init__(self, genres):
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
        self.yearEndInput.setValue(2024)
        layout.addWidget(self.yearEndInput, 1, 1)
        self.genreCombobox = QComboBox()        
        for genre in genres:
            self.genreCombobox.addItem(genre.name, genre.id)
        self.genreCombobox.setCurrentIndex(-1)
        layout.addWidget(self.genreCombobox, 1, 2)   
        
        self.clearFilters = QPushButton()
        self.clearFilters.setIcon(QtGui.QIcon(absPath("imagenes/limpiarFiltro.png")))
        self.clearFilters.setFixedSize(QSize(25,25))
        self.clearFilters.clicked.connect(self.CLEAR_FILTERS)
        layout.addWidget(self.clearFilters, 1, 3)  
        
        self.setLayout(layout)
        
    def CLEAR_FILTERS(self):
        self.artistCheckbox.setChecked(True)
        self.albumsCheckbox.setChecked(True)
        self.songsCheckbox.setChecked(True)
        self.yearStartInput.setValue(1900)
        self.yearEndInput.setValue(2024)
        self.genreCombobox.setCurrentIndex(-1)




