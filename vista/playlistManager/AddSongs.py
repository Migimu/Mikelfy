from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt,  Signal, Slot
from controlador.ControladorPlaylist import ControladorPlaylist
from vista.util.Dialogs import OPEN_ACCEPT_CANCEL_DIALOG, OPEN_INFORMATION_DIALOG

from vista.util.Utils import absPath      

class AddSongs(QWidget):
    closed = Signal()
    def __init__(self, playlist):
        super().__init__()
        self.cl:ControladorPlaylist = ControladorPlaylist()
        self.setWindowTitle("Buscador")
        self.playlist = playlist
        self.songs = self.cl.GET_SONGS()
        self.selectedSongs = self.playlist.songs
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QVBoxLayout()       

        self.name = QLineEdit(playlist.name)       
        self.name.setFixedWidth(200)         
        layout.addWidget(self.name, 1, Qt.AlignCenter)
        
        self.scroll = QScrollArea()        
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setFixedWidth(360)
        self.scroll.setFixedHeight(400)        
        self.scroll.setWidget(self.BUILD_RESULTS())
        layout.addWidget(self.scroll, 7, Qt.AlignCenter)
            
        
        buttonWidget = QWidget()
        buttonLayout = QHBoxLayout()
        
        acceptButton = QPushButton("Aceptar")
        acceptButton.setFixedWidth(100)
        acceptButton.clicked.connect(self.ACCEPT_CHANGES)
        buttonLayout.addWidget(acceptButton)
        
        cancelButton = QPushButton("Cancelar")
        cancelButton.setFixedWidth(100)
        cancelButton.clicked.connect(self.CANCEL)
        buttonLayout.addWidget(cancelButton)    
        
        buttonWidget.setLayout(buttonLayout)
        
        layout.addWidget(buttonWidget)

        layout.setSpacing(0)                                

        self.setLayout(layout)
       
    def BUILD_RESULTS(self):
       results = QWidget()
       results.setFixedWidth(350)
       resultsLayout = QVBoxLayout()
       for song in self.songs:
           if not song.id in self.playlist.songs:  
               widget = self.BUILD_SONG_CARD(song)
               resultsLayout.addWidget(widget)
       results.setLayout(resultsLayout)
       
       return results      
              
    def BUILD_SONG_CARD(self, item):
       card = QWidget()
       card.setMinimumWidth(200)
       card.setFixedHeight(60)
       cardLayout = QHBoxLayout()
       songButton = QPushButton()
       songButton.setIcon(QIcon(absPath("cancion.png")))
       songButton.setIconSize(QSize(30, 30))
       songButton.setFlat(True)
       songButton.setEnabled(False)
       cardLayout.addWidget(songButton, 1)
       cardLayout.addWidget(QLabel(item.name), 8)
       checkButton = QCheckBox()
       checkButton.toggled.connect(lambda:self.ADD_SONG(checkButton.checkState(), item.id))
       checkButton.setFixedSize(50, 50)
       cardLayout.addWidget(checkButton, 1)
       card.setLayout(cardLayout)
       
       return card  
    
    def ADD_SONG(self, estado, songId):
        if estado == Qt.Checked:
            self.selectedSongs.append(songId)
        if estado == Qt.Unchecked:
            self.selectedSongs.remove(songId)   

    def ACCEPT_CHANGES(self):
        respuesta = OPEN_ACCEPT_CANCEL_DIALOG(self, "Aceptar cambios", "¿Seguro que quieres guardar estos cambios?")
        if respuesta == QMessageBox.Ok:
            self.cl.UPDATE_PLAYLISTS( self.playlist.id, self.name.text(), self.selectedSongs)            
            OPEN_INFORMATION_DIALOG("Cambios guardados", "La cambios se han guardados correctamente")
            self.close()
    
    def CANCEL(self):
        self.close()
    
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)




