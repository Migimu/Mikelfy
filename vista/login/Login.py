from PySide6.QtGui import QIcon
from vista.Menu import Menu
from PySide6.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget, QMessageBox
from PySide6.QtCore import QSize, Qt, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.Dialogs import OPEN_ACCEPT_CANCEL_DIALOG
from vista.login.NewPassword import NewPassword
from vista.login.NewUser import NewUser
from assets.util.Utils import absPath

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.cl:ControladorLogin = ControladorLogin()
        self.passwordVisibility = False

        self.resize(500, 300)
        self.setMaximumSize(500, 300)

        formulario = QGridLayout()
             
        self.user = QLineEdit()
        self.user.setPlaceholderText("Usuario")
        self.user.setFixedWidth(125)
        self.user.setFixedHeight(30)
        
        self.password = QLineEdit()    
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.Password)    
        self.password.setFixedWidth(125)
        self.password.setFixedHeight(30)
        
        self.playButton = QPushButton()
        self.playButton.clicked.connect(self.TOGGLE_PASSWORD)
        self.playButton.setFixedSize(30, 30)
        self.playButton.setIconSize(QSize(20, 20))
        self.playButton.setIcon(QIcon(absPath("hide.png")))
        
        button = QPushButton("Iniciar sesion")
        button.setFixedWidth(85)
        button.clicked.connect(self.LOGEARSE)
        
        formulario.addWidget(self.user, 0, 1, Qt.AlignHCenter)
        formulario.addWidget(self.password, 1, 1, Qt.AlignHCenter)
        formulario.addWidget(self.playButton, 1, 2, Qt.AlignLeft)
        formulario.addWidget(button, 2, 0, 1, 3, Qt.AlignHCenter)
        
        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)

        self.show()

    def TOGGLE_PASSWORD(self):
        if self.passwordVisibility:
            self.password.setEchoMode(QLineEdit.Password)
            self.playButton.setIcon(QIcon(absPath("hide.png")))
            self.passwordVisibility = False
        else:
            self.password.setEchoMode(QLineEdit.Normal)
            self.playButton.setIcon(QIcon(absPath("show.png")))
            self.passwordVisibility = True

    def LOGEARSE(self):       
        isValid, user = self.cl.VALIDAR(self.user.text(), self.password.text())
        match(isValid):
            case -1:
                self.ASK_TO_REGISTER(user)             
            case 0:
                self.ASK_TO_CHANGE_PASSWORD(user)
            case 1:                                         
                self.OPEN_DASHBOARD_WINDOW(user)
                
    def ASK_TO_CHANGE_PASSWORD(self, user):
        respuesta = OPEN_ACCEPT_CANCEL_DIALOG(self, "Contraseña erronea", "La contraseña es erronea\n¿Quieres cambiar la contraseña?")
        if respuesta == QMessageBox.Ok:
            self.OPEN_NEW_PASSWORD_WINDOW(user)
            self.hide()
    
    def ASK_TO_REGISTER(self, username):
        respuesta = OPEN_ACCEPT_CANCEL_DIALOG(self, "Usuario no existente", "El usuario '"+ self.user.text() +"' no existe\n¿Quieres crear un usuario nuevo?")
        if respuesta == QMessageBox.Ok:
            self.OPEN_NEW_USER_WINDOW(username)
            self.hide()
    
    def OPEN_NEW_USER_WINDOW(self, username):              
        self.newUser = NewUser(username)          
        self.newUser.closed.connect(self.ON_CHILD_CLOSED)
        self.newUser.show()
        
    def OPEN_NEW_PASSWORD_WINDOW(self, user):              
        self.newPassword = NewPassword(user)          
        self.newPassword.closed.connect(self.ON_CHILD_CLOSED)
        self.newPassword.show()
        
    def OPEN_DASHBOARD_WINDOW(self, user):              
        self.menu = Menu(user)          
        self.menu.closed.connect(self.ON_CHILD_CLOSED)
        self.menu.show()
                 
            
    @Slot()
    def ON_CHILD_CLOSED(self):
        self.user.setText("")
        self.password.setText("")
        self.show()
    
    @Slot()
    def closeEvent(self, event):
        respuesta = OPEN_ACCEPT_CANCEL_DIALOG(self, "Adios", "¿Seguro que quieres cerrar el programa?")
        if respuesta == QMessageBox.Ok:
            self.cl.LOGOUT()
            super().closeEvent(event)
