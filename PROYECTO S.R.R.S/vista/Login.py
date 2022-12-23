from PyQt5 import QtWidgets, uic
from Vista.VentanaPrincipalB import Ventanab
from Vista.VentanaPrincipalA import Ventanaa


qtCreatorFile = "UI_GRUPO5/UI/Login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        uic.loadUi("UI_GRUPO5/UI/Login.ui", self)
        self.btnInicio.clicked.connect(self.iniciarSesion)
        self.show()
    

    
    def iniciarSesion(self):
        usuario=self.txtUsuario.text()
        contraseña=self.txtPassword.text()
        if usuario=="PL" and contraseña=="12345":
            self.close()
            ventanab=Ventanab(self)
            ventanab.show()

    
        if usuario=="IA" and contraseña=="12345" or usuario=="ST" and contraseña=="12345" or usuario=="JL" and contraseña=="12345":
            self.close()
            ventanaa=Ventanaa(self)
            ventanaa.show()

        """else: 
            mensaje=QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Portal de registros")
            mensaje.setText("Datos ingresados Incorrectos")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)
            x=mensaje.exec_()"""
            



