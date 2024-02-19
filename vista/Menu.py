import sys
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.user = user()
        
        self.resize(500, 300)
        self.setMaximumSize(500, 300)

        formulario = QGridLayout()            
        
        browserIcon = QtGui.QPixmap("printer.tif")
        buttonBrowser = QPushButton("Buscar")
        buttonBrowser.setIcon(browserIcon)
        buttonBrowser.setFixedWidth(75)
        buttonBrowser.clicked.connect(self.OPEN_BROWSER_WINDOW)
        
        playlistsIcon = QtGui.QPixmap("printer.tif")
        buttonPlaylists = QPushButton("Mis Playlists")
        buttonBrowser.setIcon(playlistsIcon)
        buttonPlaylists.setFixedWidth(75)
        buttonPlaylists.clicked.connect(self.OPEN_PLAYLISTS_WINDOW)
        
        logoutIcon = QtGui.QPixmap("printer.tif")
        buttonLogout = QPushButton("Salir")
        buttonLogout.setIcon(logoutIcon)
        buttonLogout.setFixedWidth(75)
        buttonLogout.clicked.connect(self.LOGOUT)
        
        formulario.addWidget(buttonBrowser, 0, 0, Qt.AlignRight)
        formulario.addWidget(buttonPlaylists, 0, 1, Qt.AlignLeft)
        formulario.addWidget(buttonLogout, 0, 2, Qt.AlignRight)
        
        widget = QtWidgets()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)

        self.show()                
    
    def OPEN_BROWSER_WINDOW(self):              
        # self.newUser = NewUser(username)          
        # self.newUser.closed.connect(self.ON_CHILD_CLOSED)
        # self.newUser.show()
        pass
        
    def OPEN_PLAYLISTS_WINDOW(self):              
        # self.newPassword = NewPassword(user)          
        # self.newPassword.closed.connect(self.ON_CHILD_CLOSED)
        # self.newPassword.show()
        pass
        
    def LOGOUT(self):              
        pass
                 
            
    @Slot()
    def ON_CHILD_CLOSED(self):
        self.user.setText("")
        self.password.setText("")
        self.show()

# Creamos la aplicación, la ventana e iniciamos el bucle
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())



