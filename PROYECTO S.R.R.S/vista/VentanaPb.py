from PyQt5 import QtWidgets, uic
from Vista.VentanaRegistrors import Ventanaregistrors
from Vista.VentanaRegistrop import Ventanaregistrop


class Ventanab(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ventanab, self).__init__(parent)
        uic.loadUi("UI_GRUPO5/UI/VPRINCIPALB.ui", self)

        self.btnSalir.clicked.connect(self.salir)
        self.btnRegistro.clicked.connect(self.abrirVentanars)
        
        
        
    def abrirVentanars(self):
        ventanars=Ventanaregistrors(self)
        ventanars.show()
    def abrirVentanaRegistrop(self):
        ventanarp=Ventanaregistrop(self)
        ventanarp.show()


    def salir(self):
        self.close()
    