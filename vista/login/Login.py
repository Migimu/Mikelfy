
from PySide6.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget, QMessageBox
from PySide6.QtCore import Qt, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.Dialogs import OPEN_ACCEPT_CANCEL_DIALOG
from vista.login.NewPassword import NewPassword
from vista.login.NewUser import NewUser

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cl:ControladorLogin = ControladorLogin()
        
        self.resize(500, 300)
        self.setMaximumSize(500, 300)

        formulario = QGridLayout()
             
        userLabel = QLabel("Usuario: ")
        self.user = QLineEdit()
        self.user.setFixedWidth(125)
        
        passwordLabel = QLabel("Contrasenia: ")
        self.password = QLineEdit()    
        self.password.setEchoMode(QLineEdit.Password)    
        self.password.setFixedWidth(125)
        
        button = QPushButton("Aceptar")
        button.setFixedWidth(75)
        button.clicked.connect(self.LOGEARSE)
        
        formulario.addWidget(userLabel, 0, 0, Qt.AlignRight)
        formulario.addWidget(self.user, 0, 1, Qt.AlignLeft)
        formulario.addWidget(passwordLabel, 1, 0, Qt.AlignRight)
        formulario.addWidget(self.password, 1, 1, Qt.AlignLeft)
        formulario.addWidget(button, 2, 0, 1, 2, Qt.AlignHCenter)
        
        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)

        self.show()


    def LOGEARSE(self):       
        isValid, user = self.cl.VALIDAR(self.user.text(), self.password.text())
        match(isValid):
            case -1:
                self.ASK_TO_REGISTER(user)             
            case 0:
                self.ASK_TO_CHANGE_PASSWORD(user)
            case 1:                                         
                self.OPEN_DASHBOARD_WINDOW()
                
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
        
    def OPEN_DASHBOARD_WINDOW(self):              
        pass
                 
            
    @Slot()
    def ON_CHILD_CLOSED(self):
        self.user.setText("")
        self.password.setText("")
        self.show()

            

# Creamos la aplicación, la ventana e iniciamos el bucle
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
