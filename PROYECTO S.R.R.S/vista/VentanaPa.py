from PyQt5 import QtWidgets, uic
from Vista.VentanaRegistrors import Ventanaregistrors
from Vista.VentanaRegistrop import Ventanaregistrop
from Vista.VentanaReporte import Ventanareportes


class Ventanaa(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ventanaa, self).__init__(parent)
        uic.loadUi("UI_GRUPO5/UI/VPRINCIPALA.ui", self)

        self.btnSalir.clicked.connect(self.salir)
        self.btnRegistro.clicked.connect(self.abrirVentanars)
        self.btnPersonal.clicked.connect(self.abrirVentanaPersonal)
        self.btnReporte.clicked.connect(self.abrirVentanaReporte)
        
    def abrirVentanars(self):
        ventanars=Ventanaregistrors(self)
        ventanars.show()

    def abrirVentanaPersonal(self):
        ventanarp=Ventanaregistrop(self)
        ventanarp.show()

    def abrirVentanaReporte(self):
        ventanarep=Ventanareportes(self)
        ventanarep.show()

    def salir(self):
        self.close()
