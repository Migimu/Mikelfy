import sys
from PySide6.QtWidgets import QApplication
from modelo.Conn import CONEXION
from vista.login.Login import MainWindow

if __name__ == "__main__":   

    app = QApplication(sys.argv)
    conn = CONEXION()
    conn.LOAD_DATA()                  
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





