from PySide6.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Qt,  Signal, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.Dialogs import OPEN_INFORMATION_DIALOG

class NewPassword(QWidget):
    closed = Signal()
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.cl:ControladorLogin = ControladorLogin()

        self.resize(500, 300)
        self.setMaximumSize(500, 300)

        formulario = QGridLayout()
             
        passwordLabel = QLabel("Contraseña: ")
        self.password = QLineEdit()
        self.password.setFixedWidth(125)
        
        newPasswordLabel = QLabel("Repita contraseña: ")
        self.newPassword = QLineEdit()    
        self.newPassword.setFixedWidth(125)
        
        button = QPushButton("Aceptar")
        button.setFixedWidth(75)
        button.clicked.connect(self.CAMBIAR)
        
        formulario.addWidget(passwordLabel, 0, 0, Qt.AlignRight)
        formulario.addWidget(self.password, 0, 1, Qt.AlignLeft)
        formulario.addWidget(newPasswordLabel, 1, 0, Qt.AlignRight)
        formulario.addWidget(self.newPassword, 1, 1, Qt.AlignLeft)
        formulario.addWidget(button, 2, 0, 1, 2, Qt.AlignHCenter)
        
        self.setLayout(formulario)

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