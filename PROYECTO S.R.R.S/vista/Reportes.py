from PyQt5 import QtWidgets, uic

class Ventanareportes(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ventanareportes, self).__init__(parent)
        uic.loadUi("UI_GRUPO5/UI/REPORTESRS.ui", self)

        self.btnSalir_3.clicked.connect(self.salir)

    def salir(self):
        self.close()