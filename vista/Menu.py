from PySide6 import QtGui
from PySide6.QtCore import QSize, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QMessageBox, QPushButton, QWidget
from vista.browser.Browser import Browser

from vista.util.Dialogs import OPEN_ACCEPT_CANCEL_DIALOG
from vista.playlistManager.PlaylistManager import PlaylistManager
from vista.util.Utils import absPath


class Menu(QWidget):
    closed = Signal()
    
    def __init__(self, user):
        super().__init__()
        self.user = user
        
        self.resize(500, 300)
        self.setMaximumSize(500, 300)
        self.setWindowTitle("Menu")

        formulario = QGridLayout()            
        
        buttonBrowser = QPushButton()
        buttonBrowser.setIcon(QtGui.QIcon(absPath("imagenes/buscar.png")))
        buttonBrowser.setIconSize(QSize(35, 35))
        buttonBrowser.setToolTip("Buscar")
        buttonBrowser.setFixedWidth(75)
        buttonBrowser.setFixedHeight(75)
        buttonBrowser.clicked.connect(self.OPEN_BROWSER_WINDOW)
        
        buttonPlaylists = QPushButton()
        buttonPlaylists.setIcon(QtGui.QIcon(absPath("imagenes/listaDeReproduccion.png")))
        buttonPlaylists.setIconSize(QSize(35, 35))
        buttonPlaylists.setToolTip("Mis Playlists")
        buttonPlaylists.setFixedWidth(75)
        buttonPlaylists.setFixedHeight(75)
        buttonPlaylists.clicked.connect(self.OPEN_PLAYLISTS_WINDOW)
        
        buttonLogout = QPushButton()
        buttonLogout.setIcon(QtGui.QIcon(absPath("imagenes/cerrarSesion.png")))
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

# Creamos la aplicación, la ventana e iniciamos el bucle



