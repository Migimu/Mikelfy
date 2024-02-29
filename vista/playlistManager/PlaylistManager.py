from PySide6 import QtGui
from PySide6.QtCore import QSize, Qt, Signal, Slot
from PySide6.QtWidgets import QHBoxLayout, QLabel, QMessageBox, QPushButton, QScrollArea, QVBoxLayout, QWidget

from controlador.ControladorPlaylist import ControladorPlaylist
from vista.util.Dialogs import OPEN_ACCEPT_CANCEL_DIALOG, OPEN_INFORMATION_DIALOG, OPEN_TEXT_INPUT_DIALOG
from vista.util.MediaPlayer import MediaPlayer
from vista.util.Utils import absPath


class PlaylistManager(QWidget):
    closed = Signal()
    mainLayout = QVBoxLayout()
    def __init__(self, userId):
        super().__init__()
        self.setWindowTitle("Gestor lista de reproducciones")
        self.userId = userId
        self.selectedPlaylist = None
        self.cl:ControladorPlaylist = ControladorPlaylist()
        self.searchText = ""
        self.resize(600, 400)
        self.setMaximumSize(600, 400)
        self.BUILD_MAIN_LAYOUT()
        self.setLayout(self.mainLayout)
        
    def BUILD_MAIN_LAYOUT(self):
        
        for i in reversed(range(self.mainLayout.count())): 
            self.mainLayout.itemAt(i).widget().deleteLater()

        backButton = QPushButton()
        backButton.clicked.connect(self.VOLVER)
        backButton.setIcon(QtGui.QIcon(absPath("imagenes/back.png")))
        backButton.setFixedSize(QSize(30,30))
        self.mainLayout.addWidget(backButton, 1, Qt.AlignLeft)
        
        gestor = QWidget()
        gestor.setLayout(self.BUILD_MANAGER_LAYOUT())
        self.mainLayout.addWidget(gestor)
       
        mediaPlayer = MediaPlayer()
        mediaPlayer.setFixedWidth(600)
        self.mainLayout.addWidget(mediaPlayer, 1, Qt.AlignCenter)
        
        
    def BUILD_MANAGER_LAYOUT(self):
        managerLayout = QHBoxLayout()
        
        self.playlistList = QScrollArea()     
        list = QWidget()
        self.playlistList.setFixedHeight(300)     
        listaLayout = QVBoxLayout()
        
        playlists = self.cl.GET_USER_PLAYLISTS(self.userId)
        for playlist in playlists:
            listaLayout.addWidget(self.BUILD_PLAYLIST_CARD(playlist))
        listaLayout.addWidget(self.BUILD_ADD_PLAYLIST_CARD())
            
        list.setLayout(listaLayout)
        self.playlistList.setWidget(list)
        managerLayout.addWidget(self.playlistList, 5)
       
        if self.selectedPlaylist == None:
            labelNada = QLabel("Selecciona una playlist")           
            managerLayout.addWidget(labelNada, 5, Qt.AlignCenter)
        else:
            self.vistaList = QScrollArea()
            self.vista = QWidget()
            self.vista.setFixedWidth(265)
            self.vistaList.setFixedHeight(300)
            vistaLayout = QVBoxLayout()
            vistaLayout.setContentsMargins(0, 0, 0, 0)

            # vistaLayout.setSpacing(0)
            nameLabel = QLabel(self.selectedPlaylist.name)
            nameLabel.setFixedHeight(100)
            nameLabel.setAlignment(Qt.AlignCenter)
            nameLabel.setStyleSheet("""QLabel {
                                        border: 1px solid black;
                                        font-size: 32px;
                                    }""")
            # vistaLayout.addWidget(self.BUILD_ADD_SONG_CARD())
            vistaLayout.addWidget(nameLabel) 
            for song in self.cl.GET_SONGS_BY_ID(self.selectedPlaylist.songs):
                vistaLayout.addWidget(self.BUILD_SONG_CARD(song))          
            self.vista.setLayout(vistaLayout)
            self.vistaList.setWidget(self.vista)
        
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
       editButton.clicked.connect(lambda: self.EDITAR_PLAYLIST(playlist))
       cardLayout.addWidget(editButton, 1)
       deleteButton = QPushButton()
       deleteButton.setFixedSize(50, 50)
       deleteButton.setIconSize(QSize(20, 20))
       deleteButton.setIcon(QtGui.QIcon(absPath("imagenes/borrar.png")))
       deleteButton.setFlat(True)
       deleteButton.clicked.connect(lambda: self.ELIMINAR_PLAYLIST(playlist.id))
       cardLayout.addWidget(deleteButton, 1)
       card.setLayout(cardLayout)
       
       return card 
   
    def BUILD_ADD_PLAYLIST_CARD(self):
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
   
    def BUILD_ADD_SONG_CARD(self):
       card = QWidget()
       card.setFixedHeight(50)
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
   
    def BUILD_SONG_CARD(self, item):
       card = QWidget()
       cardLayout = QHBoxLayout()
       songButton = QPushButton()
       songButton.setIcon(QtGui.QIcon(absPath("imagenes/cancion.png")))
       songButton.setIconSize(QSize(30, 30))
       songButton.setFlat(True)
       songButton.setEnabled(False)
       cardLayout.addWidget(songButton, 1)
       cardLayout.addWidget(QLabel(item.name), 8)
       playButton = QPushButton()
       playButton.clicked.connect(lambda: self.QUITAR_CANCION_PLAYLIST(item.id, self.selectedPlaylist.id))
       playButton.setFixedSize(50, 50)
       playButton.setIconSize(QSize(30, 30))
       playButton.setIcon(QtGui.QIcon(absPath("imagenes/borrar.png")))
       playButton.setFlat(True)
       cardLayout.addWidget(playButton, 1)
       card.setLayout(cardLayout)
       
       return card    
    
    def CREAR_PLAYLIST(self):
       title = OPEN_TEXT_INPUT_DIALOG("Nueva lista de reproduccion", "Introduce el titulo de la nueva lista de reproduccion")
       if title != None:
           self.cl.CREATE_PLAYLISTS(title, self.userId) 
           self.REFRESCAR_PANTALLA()
           
   
    def ELIMINAR_PLAYLIST(self, id):
        respuesta = OPEN_ACCEPT_CANCEL_DIALOG(self, "Eliminar lista de repoduccion", "¿Seguro que quieres eliminar la lista de reproduccion?")
        if respuesta == QMessageBox.Ok:
            self.cl.DELETE_PLAYLISTS(id)            
            OPEN_INFORMATION_DIALOG("Eliminado correctamente", "La lista de reproduccion ha sido eliminada correctamente")
            self.REFRESCAR_PANTALLA()
            
            
    def EDITAR_PLAYLIST(self, playlist):
       self.selectedPlaylist = playlist
       self.REFRESCAR_PANTALLA()
            
    def REFRESCAR_PANTALLA(self):
        self.BUILD_MAIN_LAYOUT()
        self.setLayout(self.mainLayout)    
        
    def QUITAR_CANCION_PLAYLIST(self, songId, playlistId):
        respuesta = OPEN_ACCEPT_CANCEL_DIALOG(self, "Eliminar cancion", "¿Seguro que quieres eliminar cancion de la lista de reproduccion?")
        if respuesta == QMessageBox.Ok:
            self.cl.DELETE_SONG_FROM_PLAYLIST(playlistId, songId)            
            OPEN_INFORMATION_DIALOG("Eliminada correctamente", "La cancion ha sido eliminada correctamente")
            self.REFRESCAR_PANTALLA()
    
    def VOLVER(self):
       self.close() 
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)




