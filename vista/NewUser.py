from PySide6.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Qt,  Signal, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.Dialogs import OPEN_INFORMATION_DIALOG

class NewUser(QWidget):
    closed = Signal()
    def __init__(self, username):
        super().__init__()
        self.cl:ControladorLogin = ControladorLogin()
        
        self.resize(500, 300)
        self.setMaximumSize(500, 300)

        formulario = QGridLayout()
        
        nameLabel = QLabel("Nombre: ")
        self.name = QLineEdit()
        self.name.setFixedWidth(125)
             
        userLabel = QLabel("Usuario: ")
        self.user = QLineEdit()
        self.user.setFixedWidth(125)
        self.user.setText(username)
        
        passwordLabel = QLabel("Contraseña: ")
        self.password = QLineEdit()    
        self.password.setFixedWidth(125)
        
        button = QPushButton("Aceptar")
        button.setFixedWidth(75)
        button.clicked.connect(self.CREAR)
        
        formulario.addWidget(nameLabel, 0, 0, Qt.AlignRight)
        formulario.addWidget(self.name, 0, 1, Qt.AlignLeft)
        formulario.addWidget(userLabel, 1, 0, Qt.AlignRight)
        formulario.addWidget(self.user, 1, 1, Qt.AlignLeft)
        formulario.addWidget(passwordLabel, 2, 0, Qt.AlignRight)
        formulario.addWidget(self.password, 2, 1, Qt.AlignLeft)
        formulario.addWidget(button, 3, 0, 1, 2, Qt.AlignHCenter)
        
        self.setLayout(formulario)


    def CREAR(self):
       isValid = self.cl.RESGISTRAR(self.user.text(),self.password.text())
       if isValid:
           OPEN_INFORMATION_DIALOG("¡Enhorabuena!", "Tu usuario ha sido creado correctamente")
           self.close()
       else:
           OPEN_INFORMATION_DIALOG("¡Error!", "El usuario ya existe en la base de datos")
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)