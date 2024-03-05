from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QCalendarWidget, QComboBox, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PySide6.QtCore import QDate, QSize, Qt,  Signal, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.Dialogs import OPEN_INFORMATION_DIALOG
from assets.util.Utils import absPath

class NewUser(QWidget):
    closed = Signal()
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Nuevo usuario")
        self.passwordVisibility = False
        self.cl:ControladorLogin = ControladorLogin()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        formulario = QGridLayout()
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("Nombre")
        self.name.setFixedWidth(150)
        self.name.setFixedHeight(30)
             
        self.user = QLineEdit()
        self.user.setPlaceholderText("Usuario")
        self.user.setFixedWidth(150)
        self.user.setFixedHeight(30)
        self.user.setText(username)
        
        self.email = QLineEdit()    
        self.email.setPlaceholderText("Email")
        self.email.setFixedWidth(150)
        self.email.setFixedHeight(30)
        
        self.country =  QComboBox()
        for count in self.cl.GET_COUNTRIES():
            self.country.addItem(count.name, count.id)
        self.country.setCurrentIndex(-1)
        
        self.birthDate = QCalendarWidget()    
        self.birthDate.setMinimumDate(QDate(1900, 1 , 1))
        self.birthDate.setMaximumDate(QDate.currentDate())
        self.birthDate.setFixedWidth(150)
        
        self.password = QLineEdit()    
        self.password.setEchoMode(QLineEdit.Password)  
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedWidth(150)
        self.password.setFixedHeight(30)
        
        self.passwordButton = QPushButton()
        self.passwordButton.clicked.connect(self.TOGGLE_PASSWORD)
        self.passwordButton.setFixedSize(30, 30)
        self.passwordButton.setIconSize(QSize(20, 20))
        self.passwordButton.setIcon(QIcon(absPath("hide.png")))
        
        buttonAccept = QPushButton("Aceptar")
        buttonAccept.setFixedWidth(75)
        buttonAccept.clicked.connect(self.CREAR)
        
        buttonClose = QPushButton("Cancelar")
        buttonClose.setFixedWidth(75)
        buttonClose.clicked.connect(self.close)
        
        formulario.addWidget(self.name, 0, 1, Qt.AlignHCenter)      
        formulario.addWidget(self.user, 1, 1, Qt.AlignHCenter)       
        formulario.addWidget(self.email, 2, 1, Qt.AlignHCenter)        
        formulario.addWidget(self.country, 3, 1, Qt.AlignHCenter)       
        formulario.addWidget(self.birthDate, 4, 1, Qt.AlignHCenter)
        formulario.addWidget(self.password, 5, 1, Qt.AlignHCenter)
        formulario.addWidget(self.passwordButton, 5, 2, Qt.AlignLeft)
        
        formulario.addWidget(buttonClose, 6, 0, 1, 2, Qt.AlignRight)  
        formulario.addWidget(buttonAccept, 6, 1, 1, 2, Qt.AlignLeft)   
        
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

    def CREAR(self):
       isValid = self.cl.VALIDATE_USERNAME(self.user.text())
       if (self.user.text() == '' or self.name.text() == ''  or self.email.text() == '' or self.country.currentIndex() == -1 or self.password.text() == ''):    
           OPEN_INFORMATION_DIALOG("¡Error!", "Faltan campos por rellenar")
       else:
           if isValid:
               self.cl.RESGISTRATE(self.user.text(), self.name.text(), self.email.text(), self.country.currentData(), self.birthDate.selectedDate().year(), self.password.text())
               OPEN_INFORMATION_DIALOG("¡Enhorabuena!", "Tu usuario ha sido creado correctamente")
               self.close()
           else:
               OPEN_INFORMATION_DIALOG("¡Error!", "El usuario ya existe en la base de datos")
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)