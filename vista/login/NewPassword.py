from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PySide6.QtCore import QSize, Qt, Signal, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.util.Dialogs import OPEN_INFORMATION_DIALOG
from vista.util.Utils import absPath

class NewPassword(QWidget):
    closed = Signal()
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle("Nueva contraseña")
        self.user = user
        self.passwordVisibility = False
        self.newPasswordVisibility = False
        self.cl:ControladorLogin = ControladorLogin()

        self.resize(500, 300)
        self.setMaximumSize(500, 300)

        formulario = QGridLayout()
             
        self.password = QLineEdit()
        self.password.setPlaceholderText("Nueva contraseña")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedWidth(125)
        self.password.setFixedHeight(30)
        
        self.passwordButton = QPushButton()
        self.passwordButton.clicked.connect(self.TOGGLE_PASSWORD)
        self.passwordButton.setFixedSize(30, 30)
        self.passwordButton.setIconSize(QSize(20, 20))
        self.passwordButton.setIcon(QIcon(absPath("hide.png")))
        
        self.newPassword = QLineEdit()    
        self.newPassword.setPlaceholderText("Repita contraseña")    
        self.newPassword.setEchoMode(QLineEdit.Password)    
        self.newPassword.setFixedWidth(125)
        self.newPassword.setFixedHeight(30)
        
        self.newPassworButton = QPushButton()
        self.newPassworButton.clicked.connect(self.TOGGLE_NEW_PASSWORD)
        self.newPassworButton.setFixedSize(30, 30)
        self.newPassworButton.setIconSize(QSize(20, 20))
        self.newPassworButton.setIcon(QIcon(absPath("hide.png")))
        
        buttonAccept = QPushButton("Aceptar")
        buttonAccept.setFixedWidth(75)
        buttonAccept.clicked.connect(self.CAMBIAR)
        
        buttonClose = QPushButton("Cancelar")
        buttonClose.setFixedWidth(75)
        buttonClose.clicked.connect(self.close)
        
        formulario.addWidget(self.password, 0, 1, Qt.AlignHCenter)
        formulario.addWidget(self.passwordButton, 0, 2, Qt.AlignLeft)
        formulario.addWidget(self.newPassword, 1, 1, Qt.AlignHCenter)
        formulario.addWidget(self.newPassworButton, 1, 2, Qt.AlignLeft)
        formulario.addWidget(buttonClose, 2, 0, 1, 2, Qt.AlignRight)  
        formulario.addWidget(buttonAccept, 2, 1, 1, 2, Qt.AlignLeft)        
              
        
        self.setLayout(formulario)
        
    def TOGGLE_PASSWORD(self):
        if self.passwordVisibility:
            self.password.setEchoMode(QLineEdit.Password)
            self.passwordButton.setIcon(QIcon(absPath("hide.png")))
            self.passwordVisibility = False
        else:
            self.password.setEchoMode(QLineEdit.Normal)
            self.passwordButton.setIcon(QIcon(absPath("show.png")))
            self.passwordVisibility = True
            
    def TOGGLE_NEW_PASSWORD(self):
        if self.newPasswordVisibility:
            self.newPassword.setEchoMode(QLineEdit.Password)
            self.newPassworButton.setIcon(QIcon(absPath("hide.png")))
            self.newPasswordVisibility = False
        else:
            self.newPassword.setEchoMode(QLineEdit.Normal)
            self.newPassworButton.setIcon(QIcon(absPath("show.png")))
            self.newPasswordVisibility = True

    def CAMBIAR(self):
       isValid = self.cl.VALIDATE_PASSWORD(self.user, self.password.text(),self.newPassword.text())
       match(isValid):
            case -1:
                OPEN_INFORMATION_DIALOG("¡Error!", "Las contraseñas no coinciden")             
            case 0:
                OPEN_INFORMATION_DIALOG("¡Error!", "Por favor utiliza una nueva contraseña")
            case 1:    
                self.cl.CHANGE_PASSWORD(self.user.id, self.newPassword.text())
                OPEN_INFORMATION_DIALOG("¡Enhorabuena!", "La contraseña a sido cambiada")
                self.close()          
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)