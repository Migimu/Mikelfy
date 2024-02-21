from PySide6.QtWidgets import QCalendarWidget, QComboBox, QHBoxLayout, QLineEdit, QLabel, QPushButton, QGridLayout, QVBoxLayout, QWidget
from PySide6.QtCore import Qt,  Signal, Slot

from controlador.ControladorLogin import ControladorLogin
from vista.Dialogs import OPEN_INFORMATION_DIALOG


class Searchbar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QHBoxLayout()

        # le añadimos unas cuantas cajas
        layout.addWidget(QLineEdit(), 8)
        # layout.addWidget(Caja("blue"))
        layout.addWidget(QPushButton(), 1)
        layout.addWidget(QPushButton(), 1)

        # modificamos los márgenes
        layout.setContentsMargins(0, 0, 0, 0)

        # modificamos el espaciado
        layout.setSpacing(0)                     
        
        self.setLayout(layout)

class Browser(QWidget):
    closed = Signal()
    def __init__(self, user):
        super().__init__()
        self.user = user
        # self.cl:ControladorLogin = ControladorLogin()
        
        self.resize(600, 400)
        self.setMaximumSize(600, 400)

        layout = QVBoxLayout()

        # le añadimos unas cuantas cajas
        layout.addWidget(Searchbar(), 1)
        # layout.addWidget(Caja("blue"))
        layout.addWidget(QLabel("No hay nada"), 9, Qt.AlignHCenter)

        # modificamos los márgenes
        # layout.setContentsMargins(0, 0, 0, 0)

        # modificamos el espaciado
        layout.setSpacing(0)                     
        
        self.setLayout(layout)


    def CREAR(self):
       pass
           
    @Slot()
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)


