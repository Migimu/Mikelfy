from PySide6 import QtGui
from PySide6.QtCore import QSize, Qt, Signal, Slot
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget

from controlador.ControladorPlaylist import ControladorPlaylist
from vista.util.Dialogs import OPEN_TEXT_INPUT_DIALOG
from vista.util.MediaPlayer import MediaPlayer
from vista.util.Utils import absPath


class PlaylistManager(QWidget):
    closed = Signal()
    gestor = None
    def __init__(self, userId):
        super().__init__()
        self.setWindowTitle("Gestor lista de reproducciones")
        self.userId = userId
        self.cl:ControladorPlaylist = ControladorPlaylist()
        self.searchText = ""
        self.resize(600, 400)
        self.setMaximumSize(600, 400)
        
        mainLayout = QVBoxLayout()
        
        backButton = QPushButton()
        backButton.clicked.connect(self.VOLVER)
        backButton.setIcon(QtGui.QIcon(absPath("imagenes/back.png")))
        backButton.setFixedSize(QSize(30,30))
        mainLayout.addWidget(backButton, 1, Qt.AlignLeft)
        
        self.gestor = QWidget()
        self.gestor.setLayout(self.BUILD_MANAGER_LAYOUT())
        mainLayout.addWidget(self.gestor)
       
        mediaPlayer = MediaPlayer()
        mediaPlayer.setFixedWidth(600)
        mainLayout.addWidget(mediaPlayer, 1, Qt.AlignCenter)

        self.setLayout(mainLayout)
        
    def BUILD_MANAGER_LAYOUT(self):
        managerLayout = QHBoxLayout()
        
        self.playlistList = QScrollArea()
        lista = QWidget()      
        listaLayout = QVBoxLayout()
        
        playlists = self.cl.GET_USER_PLAYLISTS(self.userId)
        for playlist in playlists:
            listaLayout.addWidget(self.BUILD_PLAYLIST_CARD(playlist))
        listaLayout.addWidget(self.BUILD_ADD_CARD())
            
        lista.setLayout(listaLayout)
        self.playlistList.setWidget(lista)
        managerLayout.addWidget(self.playlistList, 5)

        self.vistaList = QScrollArea()
        self.vistaList.setAlignment(Qt.AlignCenter)
        vista = QWidget()
        vistaLayout = QVBoxLayout()
        
        labelNada = QLabel("Selecciona una playlist")
        vistaLayout.addWidget(labelNada)      

        vista.setLayout(vistaLayout)
        self.vistaList.setWidget(vista)
        managerLayout.addWidget(self.vistaList, 5)
        
        return managerLayout
    
    def BUILD_PLAYLIST_CARD(self, playlist):
       card = QWidget()
       cardLayout = QHBoxLayout()
       playlistButton = QPushButton()
       playlistButton.setIcon(QtGui.QIcon(absPath("imagenes/playlist.png")))
       playlistButton.setIconSize(QSize(30, 30))
       playlistButton.setFlat(True)
       playlistButton.setEnabled(False)
       cardLayout.addWidget(playlistButton, 1)
       cardLayout.addWidget(QLabel(playlist.name), 7)
       editButton = QPushButton()
       editButton.setFixedSize(50, 50)
       editButton.setIconSize(QSize(20, 20))
       editButton.setIcon(QtGui.QIcon(absPath("imagenes/editar.png")))
       editButton.setFlat(True)
       cardLayout.addWidget(editButton, 1)
       deleteButton = QPushButton()
       deleteButton.setFixedSize(50, 50)
       deleteButton.setIconSize(QSize(20, 20))
       deleteButton.setIcon(QtGui.QIcon(absPath("imagenes/borrar.png")))
       deleteButton.setFlat(True)
       cardLayout.addWidget(deleteButton, 1)
       card.setLayout(cardLayout)
       
       return card 
   
    def BUILD_ADD_CARD(self):
       card = QWidget()
       cardLayout = QHBoxLayout()
       iconButton = QPushButton()
       iconButton.setIcon(QtGui.QIcon(absPath("imagenes/addPlaylist.png")))
       iconButton.setIconSize(QSize(30, 30))
       iconButton.setFlat(True)
       iconButton.setEnabled(False)
       cardLayout.addWidget(iconButton, 1)
       artistNameButton = QPushButton("Nueva playlist")
       artistNameButton.setStyleSheet("text-align:left;")
       artistNameButton.setFixedHeight(50)
       artistNameButton.clicked.connect(self.CREAR_PLAYLIST)
       artistNameButton.setFlat(True)
       cardLayout.addWidget(artistNameButton, 9)
       card.setLayout(cardLayout)
       
       return card 
    
    def CREAR_PLAYLIST(self):
       title = OPEN_TEXT_INPUT_DIALOG("Nueva lista de reproduccion", "Introduce el titulo de la playlist")
       if title != None:
           self.cl.CREATE_PLAYLISTS(title, self.userId) 
           self.gestor.setLayout(self.BUILD_MANAGER_LAYOUT())
           self.gestor.update()
           # 
   
    def ELIMINAR_PLAYLIST(self):
       pass 
    
    def VOLVER(self):
       self.close() 
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)




