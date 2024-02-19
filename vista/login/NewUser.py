from PySide6.QtWidgets import QCalendarWidget, QComboBox, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Qt,  Signal, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.Dialogs import OPEN_INFORMATION_DIALOG

class NewUser(QWidget):
    closed = Signal()
    def __init__(self, username):
        super().__init__()
        self.cl:ControladorLogin = ControladorLogin()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        formulario = QGridLayout()
        
        nameLabel = QLabel("Nombre: ")
        self.name = QLineEdit()
        self.name.setFixedWidth(150)
             
        userLabel = QLabel("Usuario: ")
        self.user = QLineEdit()
        self.user.setFixedWidth(150)
        self.user.setText(username)
        
        emailLabel = QLabel("Email: ")
        self.email = QLineEdit()    
        self.email.setFixedWidth(150)
        
        countryLabel = QLabel("Pais: ")
        self.country =  QComboBox()
        self.country.addItems(['España', 'Francia', 'Portugal', 'Alemania'])
        
        birthDateLabel = QLabel("Fecha de nacimiento: ")
        self.birthDate = QCalendarWidget()    
        self.birthDate.setFixedWidth(150)
        
        passwordLabel = QLabel("Contraseña: ")
        self.password = QLineEdit()    
        self.password.setEchoMode(QLineEdit.Password)  
        self.password.setFixedWidth(150)
        
        button = QPushButton("Aceptar")
        button.setFixedWidth(75)
        button.clicked.connect(self.CREAR)
        
        formulario.addWidget(nameLabel, 0, 0, Qt.AlignRight)
        formulario.addWidget(self.name, 0, 1, Qt.AlignLeft)
        
        formulario.addWidget(userLabel, 1, 0, Qt.AlignRight)
        formulario.addWidget(self.user, 1, 1, Qt.AlignLeft)
        
        formulario.addWidget(emailLabel, 2, 0, Qt.AlignRight)
        formulario.addWidget(self.email, 2, 1, Qt.AlignLeft)
        
        formulario.addWidget(countryLabel, 3, 0, Qt.AlignRight)
        formulario.addWidget(self.country, 3, 1, Qt.AlignLeft)
        
        formulario.addWidget(birthDateLabel, 4, 0, Qt.AlignRight)
        formulario.addWidget(self.birthDate, 4, 1, Qt.AlignLeft)

        formulario.addWidget(passwordLabel, 5, 0, Qt.AlignRight)
        formulario.addWidget(self.password, 5, 1, Qt.AlignLeft)
        formulario.addWidget(button, 6, 0, 1, 2, Qt.AlignHCenter)
        
        self.setLayout(formulario)


    def CREAR(self):
       isValid = self.cl.VALIDATE_USERNAME(self.user.text())
       if isValid:
           self.cl.RESGISTRATE(self.user.text(), self.name.text(), self.email.text(), self.country.currentIndex(), self.birthDate.selectedDate(), self.password.text())
           OPEN_INFORMATION_DIALOG("¡Enhorabuena!", "Tu usuario ha sido creado correctamente")
           self.close()
       else:
           OPEN_INFORMATION_DIALOG("¡Error!", "El usuario ya existe en la base de datos")
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)