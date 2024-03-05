from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QMessageBox, QPushButton, QWidget
from controlador.clases.User import User
from vista.browser.Browser import Browser

from vista.Dialogs import OPEN_ACCEPT_CANCEL_DIALOG
from vista.playlistManager.PlaylistManager import PlaylistManager
from assets.util.Utils import absPath


class Menu(QWidget):
    closed = Signal()
    
    def __init__(self, user: User):
        super().__init__()
        self.user = user
        
        self.resize(500, 300)
        self.setMaximumSize(500, 300)
        self.setWindowTitle("Bievenid@ "+ user.username)

        formulario = QGridLayout()            
        
        buttonBrowser = QPushButton()
        buttonBrowser.setIcon(QIcon(absPath("buscar.png")))
        buttonBrowser.setIconSize(QSize(35, 35))
        buttonBrowser.setToolTip("Buscar")
        buttonBrowser.setFixedWidth(75)
        buttonBrowser.setFixedHeight(75)
        buttonBrowser.clicked.connect(self.OPEN_BROWSER_WINDOW)
        
        buttonPlaylists = QPushButton()
        buttonPlaylists.setIcon(QIcon(absPath("listaDeReproduccion.png")))
        buttonPlaylists.setIconSize(QSize(35, 35))
        buttonPlaylists.setToolTip("Mis Playlists")
        buttonPlaylists.setFixedWidth(75)
        buttonPlaylists.setFixedHeight(75)
        buttonPlaylists.clicked.connect(self.OPEN_PLAYLISTS_WINDOW)
        
        buttonLogout = QPushButton()
        buttonLogout.setIcon(QIcon(absPath("cerrarSesion.png")))
        buttonLogout.setIconSize(QSize(35, 35))
        buttonLogout.setToolTip("Salir")
        buttonLogout.setFixedWidth(75)
        buttonLogout.setFixedHeight(75)
        buttonLogout.clicked.connect(self.LOGOUT)
        
        formulario.addWidget(buttonBrowser, 0, 0)
        formulario.addWidget(buttonPlaylists, 0, 1)
        formulario.addWidget(buttonLogout, 0, 2)
        
        self.setLayout(formulario)
            
    
    def OPEN_BROWSER_WINDOW(self):              
        self.browser = Browser(self.user)          
        self.browser.closed.connect(self.ON_CHILD_CLOSED)
        self.browser.show()
        
    def OPEN_PLAYLISTS_WINDOW(self):              
        self.playlistManager = PlaylistManager(self.user.id)          
        self.playlistManager.closed.connect(self.ON_CHILD_CLOSED)
        self.playlistManager.show()
        pass
        
    def LOGOUT(self):              
        respuesta = OPEN_ACCEPT_CANCEL_DIALOG(self, "Adios", "¿Seguro que quieres cerrar sesion?")
        if respuesta == QMessageBox.Ok:
            self.close()
                 
            
    @Slot()
    def ON_CHILD_CLOSED(self):
        self.show()

    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)
# Creamos la aplicación, la ventana e iniciamos el bucle



