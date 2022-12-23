from PyQt5 import QtWidgets, uic

lista=[]

class Ventanaregistrors(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ventanaregistrors, self).__init__(parent)
        uic.loadUi("UI_GRUPO5/UI/REGISTRORS.ui", self)

        self.btnSalir_3.clicked.connect(self.salir)
        self.btnRegistrar_3.clicked.connect(self.registrar)
        self.btnLimpiar.clicked.connect(self.limpiar)


    def registrar(self):
        dni=self.txtDni.text()
        tipo=self.cboProducto.currentText()
        peso=self.txtPeso.text()
        cantidad=self.txtCantidad.text()
        fecha=self.dateTime.text() #pendiente


        datos=(str(dni),tipo,str(peso),str(cantidad),str(fecha)) ##Estos datos se añaden a la lista 
        lista.append(datos)
        self.listar()

    def listar(self): ##Este metodo permitira listar los datos de la lista a la tabla
        self.tblDatos_3.setRowCount(50)
        for i in range(len(lista)):
            self.tblDatos_3.setItem(i,0, QtWidgets.QTableWidgetItem(lista[i][0]))
            self.tblDatos_3.setItem(i,1, QtWidgets.QTableWidgetItem(lista[i][1]))
            self.tblDatos_3.setItem(i,2, QtWidgets.QTableWidgetItem(lista[i][2]))
            self.tblDatos_3.setItem(i,3, QtWidgets.QTableWidgetItem(lista[i][3]))
            self.tblDatos_3.setItem(i,4, QtWidgets.QTableWidgetItem(lista[i][4]))


    def limpiar(self):
        self.txtDni.clear()
        self.cboProducto.clear()
        self.txtPeso.clear()
        self.txtCantidad.clear()
        self.dateTime.clear()
        self.tblDatos_3.clear()



    def salir(self):
        self.close()