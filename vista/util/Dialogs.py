from PySide6.QtWidgets import QInputDialog, QMessageBox


def OPEN_ACCEPT_CANCEL_DIALOG(self, title, text, btn1 = "Aceptar", btn2 = "Cancelar"):
    dialogo = QMessageBox(self)
    dialogo.setWindowTitle(title)
    dialogo.setText(text)
    dialogo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    dialogo.button(QMessageBox.Ok).setText(btn1)
    dialogo.button(QMessageBox.Cancel).setText(btn2)
    return dialogo.exec_()

def OPEN_INFORMATION_DIALOG(title, text):
    QMessageBox.about(
            None, title,text)
    
def OPEN_TEXT_INPUT_DIALOG(title, text):
    text, result = QInputDialog.getText(
            None, title,text)
  
    if result:
        return text
